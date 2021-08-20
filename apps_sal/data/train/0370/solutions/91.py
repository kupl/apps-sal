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
        for (_, indices) in primes.items():
            for i in range(len(indices) - 1):
                (k, l) = (find(indices[i]), find(indices[i + 1]))
                if k == l:
                    continue
                if size[l] > size[k]:
                    (k, l) = (l, k)
                index[l] = k
                size[k] += size[l]
        return max(size)
        '\n        n = len(A)\n        A.sort()\n        adj = [[] for _ in range(n)]\n        for i in range(n-1):\n            for j in range(i+1,n):\n                a, b = A[i], A[j]\n                while b:\n                    a, b = b, a%b\n                if a > 1:\n                    adj[i].append(j)\n                    adj[j].append(i)\n                    \n        visited = [False]*n\n        connected = [False]*n\n        \n        def dfs(i):\n            if visited[i]:\n                return 0\n            visited[i] = True\n            connected[i] = True\n            s = 1\n            for j in adj[i]:\n                s += dfs(j)\n            return s\n        \n        M = 0\n        for i in range(n):\n            if not connected[i]:\n                M = max(M, dfs(i))\n        return M\n        '
