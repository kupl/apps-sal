from functools import lru_cache


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        N = len(A)

        def valid(x, y):
            return (math.sqrt(x + y)).is_integer()

        graph = [[] for _ in range(N)]

        for i, x in enumerate(A):
            for j in range(i):
                if valid(x, A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        @lru_cache(None)
        def dfs(node, visited):
            if visited == (1 << N) - 1:
                return 1

            ans = 0
            for val in graph[node]:
                if (visited & 1 << val) == 0:
                    ans += dfs(val, visited | 1 << val)
            return ans

        ans = sum(dfs(i, 1 << i) for i in range(N))
        count = collections.Counter(A)
        for v in count.values():
            ans //= math.factorial(v)
        return ans
