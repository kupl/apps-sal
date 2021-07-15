class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def prime_factors(num):
            '''
            For a number returns it's prime factors in
            ascending order
            Input 12, output = [2,2,3]
            '''
            pfactors = []
            factor = 2
            while num >= factor * factor:
                if num % factor == 0:
                    pfactors.append(factor)
                    num = num // factor
                else:
                    factor += 1
            pfactors.append(num)
            return pfactors
        
        class DisjointSetUnion(object):
            '''
            Union Find for 0 to n (inclusive)
            '''
            def __init__(self, n):
                self.parent = {i:i for i in range(n+1)}
                self.size = [1]*(1+n)
            def find(self, x):
                if self.parent[x] != x:
                    #path compression during find
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
                # while x != self.parent[x]:
                #     x = self.parent[x]
                # return self.parent[x]
            def union(self, a, b):
                x = self.find(a)
                y = self.find(b)
                # self.parent[y] = x
                if x == y:
                    return x
                
                if self.size[x] > self.size[y]:
                    self.parent[y] = x
                    self.size[x] += self.size[y]
                    return x
                
                self.parent[x] = y
                self.size[y] += self.size[x]
                return y
        
        DS = DisjointSetUnion(max(A))
        
        #num_factor = defaultdict(list)
        num_id = defaultdict(int)
        for num in A:
            pf = list(set(prime_factors(num)))
            #num_factor[num] = pf
            num_id[num] = pf[0]
            for i in range(len(pf)-1):
                #for num pf[i] and pf[i+1] can be unioned
                DS.union(pf[i], pf[i+1]) 
        
        max_size = 0        
        #nums belong to groups which are root's of num_id[num]
        group_count = defaultdict(int)
        for num in A:
            group_id = DS.find(num_id[num])
            group_count[group_id] += 1
            max_size = max(max_size, group_count[group_id])
        
        return max_size
