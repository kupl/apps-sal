class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        N = len(A)
        maxi = max(A)
        p = [i for i in range(N)]
        size = [1] * N
        ret = 1
        primes, isPrime = [], [True] * (maxi + 1)
        for i in range(2, maxi + 1):
            if isPrime[i]: 
                primes.append(i)
                for j in range(2, maxi // i + 1):
                    isPrime[i * j] = False
        prime2Id = {}
        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]
        def union(x, y):
            nonlocal ret
            px, py = find(x), find(y)
            if px == py: return
            p[py] = px
            size[px] += size[py]
            size[py] = 0
            ret = max(ret, size[px])
            
        for i in range(N):
            a = A[i]
            for f in primes:
                if isPrime[a]:
                    if a in prime2Id: 
                        union(prime2Id[a], i)
                    prime2Id[a] = i
                    break 
                if f*f > A[i]: break
                if a % f == 0:
                    if f in prime2Id: 
                        union(prime2Id[f], i)
                    prime2Id[f] = i
                    while a % f == 0: a //= f
                if a == 1: break
        
        return ret
        

