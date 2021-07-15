'''
Start a dfs from every node not reached yet
Keep max of dfs length
Keep nodes visited and nodes to visit in dfs
'''
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        primes = []
        for x in range(2, int(max(A)**0.5)+1):
            for y in primes:
                if x % y == 0:
                    break
            else:
                primes.append(x)
    
        factors = collections.defaultdict(list)         # compute factors of each 'a'
        for a in A:
            x = a
            for p in primes:
                if p*p > x:
                    break
                if x % p == 0:
                    factors[a].append(p)
                    while x % p == 0:
                        x //= p
            if x > 1:                                   # a new prime found
                factors[a].append(x)
                primes.append(x)
                
        primes = list(set(primes))
        n = len(primes)
        p2i = {p: i for i,p in enumerate(primes)}       # prime to index
        
        parent = [i for i in range(n)]                  # union-find on primes
        
        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i,j):
            pi, pj = find(i), find(j)
            if pi != pj:
                parent[pi] = pj

        for a in A:
            if factors[a]:
                p0 = factors[a][0]
                for p in factors[a][1:]:                # link two primes if they are factors of 'a'
                    union(p2i[p0], p2i[p])
        
        count = collections.Counter(find(p2i[factors[a][0]]) for a in A if factors[a])      # each 'a' corresponds to a prime index
        return max(count.values())        
#         self.ret = float(-1)
#         self.visited = set()        
#         self.not_visited = set(A)
#         self.factors = {}
        
#         for i in A:
#             self.factors[i] = get_factors(i)
            
#         print(self.factors)
            
#         def dfs(cur, length):
#             try:
#                 self.not_visited.remove(cur)    
#             except:
#                 return

#             if length > self.ret:
#                 self.ret = length
            
#             for num in self.not_visited.copy():
#                 if num == cur:
#                     continue
                    
#                 for i in self.factors[num]:
#                     if i in self.factors[cur]:
#                         self.visited.add(num)
#                         dfs(num, length + 1)
#                         break
                        
#         for i in A:
#             dfs(i, 1)
#         return self.ret
                    
# def get_factors(x):
#     res = set()
#     for i in range(2, x + 1):
#         if x % i == 0:
#             res.add(i)
#     return res

