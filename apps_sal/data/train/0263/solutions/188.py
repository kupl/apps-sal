class Solution:
    def knightDialer(self, n: int) -> int:

        k = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        dp = [[1] * 10, [0] * 10]

        turn = 0

        for t in range(n - 1):
            turn = 1 - turn
            for i in range(10):
                dp[turn][i] = sum(dp[1 - turn][j] for j in k[i]) % (10 ** 9 + 7)

        return sum(dp[turn]) % (10 ** 9 + 7)
