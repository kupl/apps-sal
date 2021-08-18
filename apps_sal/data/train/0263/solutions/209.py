class Solution:
    def knight(self, n, current, memo):
        knight_mp = {1: {8, 6},
                     2: {9, 7},
                     3: {4, 8},
                     4: {3, 9, 0},
                     5: {},
                     6: {7, 1, 0},
                     7: {2, 6},
                     8: {3, 1},
                     9: {2, 4},
                     0: {6, 4}}

        if n == 1:
            return 1
        if (current, n) in memo:
            return memo[(current, n)]
        res = 0
        for item in knight_mp.get(current, set()):
            res += self.knight(n - 1, item, memo)

        memo[(current, n)] = res
        return res

    def knightDialer(self, n: int) -> int:

        knight_mp = {1: {8, 6},
                     2: {9, 7},
                     3: {4, 8},
                     4: {3, 9, 0},
                     5: {},
                     6: {7, 1, 0},
                     7: {2, 6},
                     8: {3, 1},
                     9: {2, 4},
                     0: {6, 4}}

        dp = [[0 if i != 0 else 1 for _ in range(0, 10)] for i in range(n)]
        mod = 10**9 + 7

        for step in range(1, n):
            for cell in range(0, 10):
                for neighbor in knight_mp.get(cell, set()):
                    dp[step][cell] += dp[step - 1][neighbor]
        return sum(dp[n - 1]) % mod
