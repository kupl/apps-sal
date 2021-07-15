class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        dic = defaultdict(list)
        
        def primefactor(x):
            s = []
            y = x
            if x % 2 == 0:
                s.append(2)
            while x%2 == 0:
                x //= 2
            for i in range(3,floor(sqrt(y))+1,2):
                if x % i == 0:
                    s.append(i)
                while x % i == 0:
                    x //= i
            if x > sqrt(y):
                s.append(x)
            return s
        
        for i in range(n):
            primes = primefactor(A[i])
            for d in primes:
                dic[d].append(i)
        a = list(range(n))
        sz = [1] * n
        
        def root(i):
            while(i != a[i]):
                a[i] = a[a[i]]
                i = a[i]
            return i
        
        def find(i,j):
            return root(i) == root(j)
            
        def union(i,j):
            root_i = root(i)
            root_j = root(j)
            if sz[root_i] > sz[root_j]:
                a[root_j] = root_i
                sz[root_i] += sz[root_j]
                sz[root_j] = 0
            else:
                a[root_i] = root_j
                sz[root_j] += sz[root_i]
                sz[root_i] = 0
            
        for v in dic.values():
            for i in range(len(v)-1):
                if find(v[i],v[i+1]) == False:
                    union(v[i],v[i+1])
        return max(sz)
