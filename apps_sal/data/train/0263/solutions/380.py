from collections import defaultdict


class Solution:

    def knightDialer(self, n: int) -> int:
        G = {1: [6, 8], 2: [7, 9], 3: [4, 8], 6: [1, 7, 0], 5: [], 4: [3, 9, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        dp = defaultdict(lambda: defaultdict(lambda: 0))

        def dfs(number, numberOfMovements):
            if numberOfMovements == 0:
                return 1
            if dp[number][numberOfMovements]:
                return dp[number][numberOfMovements]
            total = 0
            for i in G[number]:
                total += dfs(i, numberOfMovements - 1)
            dp[number][numberOfMovements] = total
            return total
        res = 0
        for i in range(10):
            res += dfs(i, n - 1)
            res = res % 1000000007
        return res
