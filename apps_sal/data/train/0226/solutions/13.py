from functools import lru_cache


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        def edge(x, y):
            r = math.sqrt(x + y)
            return int(r) ** 2 == (x + y)

        @lru_cache(None)
        def dfs(node, seen):
            if seen == (1 << N) - 1:
                return 1

            ans = 0
            for n in graph[node]:
                nxt = seen | (1 << n)
                if nxt == seen:
                    continue
                ans += dfs(n, nxt)
            return ans

        N = len(A)
        count = collections.Counter(A)
        graph = [[] for _ in range(N)]

        for i in range(N):
            for j in range(i + 1, N):
                if edge(A[i], A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        ans = sum(dfs(i, 1 << i) for i in range(N))
        for v in count.values():
            ans //= math.factorial(v)

        return ans
