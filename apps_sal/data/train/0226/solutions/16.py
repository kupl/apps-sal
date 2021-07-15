from functools import lru_cache

class Solution:
    def numSquarefulPerms(self, A):
        N = len(A)

        def edge(x, y):
            r = math.sqrt(x+y)
            return int(r + 0.5) ** 2 == x+y

        graph = [[] for _ in range(len(A))]
        for i, x in enumerate(A):
            for j in range(i):
                if edge(x, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # find num of hamiltonian paths in graph

        @lru_cache(None)
        def dfs(node, visited):
            if visited == (1 << N) - 1:
                return 1

            ans = 0
            for nei in graph[node]:
                if (visited >> nei) & 1 == 0:
                    ans += dfs(nei, visited | (1 << nei))
            return ans

        ans = sum(dfs(i, 1<<i) for i in range(N))
        count = collections.Counter(A)
        for v in count.values():
            ans //= math.factorial(v)
        return ans
