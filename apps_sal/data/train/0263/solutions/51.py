class Solution:
    def knightDialer(self, n: int) -> int:
        dp = [1] * 10
        states = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        mod = int(1e9) + 7
        for i in range(n - 1):
            dp1 = [0] * 10

            for j, st in list(states.items()):
                for k in st:
                    dp1[k] += dp[j]
                    dp1[k] %= mod
            dp = dp1
        return sum(dp) % mod
