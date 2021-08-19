class Solution:

    def knightDialer(self, n: int) -> int:
        knight_graph = {1: (8, 6), 2: (7, 9), 3: (8, 4), 4: (3, 9, 0), 5: (), 6: (7, 1, 0), 7: (2, 6), 8: (1, 3), 9: (4, 2), 0: (4, 6)}
        memo = {}
        MOD = pow(10, 9) + 7

        def btHelper(coordinate, n):
            if n == 0:
                return 1
            possibility = 0
            for avail_node in knight_graph[coordinate]:
                if (avail_node, n - 1) in memo:
                    possibility += memo[avail_node, n - 1]
                else:
                    possibility += btHelper(avail_node, n - 1)
            memo[coordinate, n] = possibility % MOD
            return possibility
        ans = 0
        for i in range(10):
            ans += btHelper(i, n - 1)
        return ans % MOD
