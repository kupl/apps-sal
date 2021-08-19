class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        graph = {1: (6, 8), 2: (9, 7), 3: (4, 8), 4: (9, 3, 0), 5: (), 6: (7, 1, 0), 7: (2, 6), 8: (1, 3), 9: (4, 2), 0: (4, 6)}
        count = 0
        MOD = 10 ** 9 + 7
        memo = collections.defaultdict(list)

        def dfs(cur, graph, n, memo):
            if n == 0:
                return 1
            if (n, cur) in memo:
                return memo[n, cur]
            count = 0
            for nei in graph[cur]:
                count += dfs(nei, graph, n - 1, memo) % MOD
            memo[n, cur] = count
            return count
        for nei in range(10):
            memo[nei] = []
            count += dfs(nei, graph, n - 1, memo) % MOD
        return count % MOD
