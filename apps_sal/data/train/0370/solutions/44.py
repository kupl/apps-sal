# class UnionFind:
#     def __init__(self, nums):
#         self.parents = {num: num for num in nums}
#         self.ranks = {num: 1 for num in nums}
    
#     def find(self, src):
#         if self.parents[src] == src:
#             return src
        
#         self.parents[src] = self.find(self.parents[src])
#         return self.parents[src]

#     def union(self, src, dest):
#         rootSrc, rootDest = self.find(src), self.find(dest)
#         if rootSrc == rootDest:
#             return -1
        
#         if self.ranks[rootSrc] > self.ranks[rootDest]:
#             self.parents[rootDest] = rootSrc
#             self.ranks[rootSrc] += self.ranks[rootDest]
#             return self.ranks[rootSrc]
#         else:
#             self.parents[rootSrc] = rootDest
#             self.ranks[rootDest] += self.ranks[rootSrc]
#             return self.ranks[rootDest]
        
# class Solution:
#     def largestComponentSize(self, A: List[int]) -> int:
#         def gcd(num1, num2):
#             if num1 < num2:
#                 return gcd(num2, num1)
#             if num2 == 0:
#                 return num1

#             return gcd(num2, num1 % num2)

#         uf = UnionFind(A)
#         for i in range(len(A) - 1):
#             for j in range(i + 1, len(A)):
#                 if gcd(A[i], A[j]) > 1:
#                     uf.union(A[i], A[j])
#         return max(uf.ranks.values())

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
