class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        index = list(range(n))
        size = [1] * n

        def find(i):
            while index[i] != i:
                i = index[i]
            return i

        def setPrimes(i):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    return setPrimes(i // j) | set([j])
            return set([i])

        primes = defaultdict(list)
        for i in range(n):
            s = setPrimes(A[i])
            for prime in s:
                primes[prime].append(i)

        for _, indices in primes.items():
            for i in range(len(indices) - 1):
                k, l = find(indices[i]), find(indices[i + 1])
                if k == l:
                    continue
                if size[l] > size[k]:
                    k, l = l, k
                index[l] = k
                size[k] += size[l]
        return max(size)

        '''
        n = len(A)
        A.sort()
        adj = [[] for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                a, b = A[i], A[j]
                while b:
                    a, b = b, a%b
                if a > 1:
                    adj[i].append(j)
                    adj[j].append(i)
                    
        visited = [False]*n
        connected = [False]*n
        
        def dfs(i):
            if visited[i]:
                return 0
            visited[i] = True
            connected[i] = True
            s = 1
            for j in adj[i]:
                s += dfs(j)
            return s
        
        M = 0
        for i in range(n):
            if not connected[i]:
                M = max(M, dfs(i))
        return M
        '''
