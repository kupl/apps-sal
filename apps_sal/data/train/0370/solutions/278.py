class UnionFind:
    def __init__(self, n): 
        self.ranks = [0]*n
        self.parents = [i for i in range(n)]
        
        
    def union(self, i, j): 
        pi = self.parent(i)
        pj = self.parent(j)
        if pi == pj: 
            return 
        else: 
            if self.ranks[pi] <= self.ranks[pj]: 
                self.parents[pi] = pj 
                self.ranks[pj] += 1 if self.ranks[pi] == self.ranks[pj] else 0 
            else: 
                self.parents[pj] = pi
                
    def parent(self, i): 
        if self.parents[i] != i: 
            self.parents[i] = self.parent(self.parents[i])
        return self.parents[i]

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A)+1)
        dic = {}
        for i, num in enumerate(A): 
            factor = self.decomp(num)
            dic[num] = factor[0]
            # print(num, factor)
            for i in range(0, len(factor)-1): 
                uf.union(factor[i], factor[i+1])
        
        count = collections.Counter()
        for num in A: 
            group_id = uf.parent(dic[num])
            count[group_id] += 1
        return max(count[i] for i in count)
        
    def decomp(self, num): 
        factor = 2
        ans = set()
        # print(\"num\", num)
        while num>=factor*factor: 
            if num%factor==0: 
                num //= factor 
                ans.add(factor)
            else: 
                factor += 1
        ans.add(num)
        # print(\"num end\", num)
        return list(ans)

