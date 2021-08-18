class Solution:
    def knightDialer(self, n: int) -> int:

        cell2jump = dict()
        cell2jump[1] = [6, 8]
        cell2jump[2] = [7, 9]
        cell2jump[3] = [4, 8]
        cell2jump[4] = [3, 9, 0]
        cell2jump[5] = []
        cell2jump[6] = [1, 7, 0]
        cell2jump[7] = [2, 6]
        cell2jump[8] = [1, 3]
        cell2jump[9] = [2, 4]
        cell2jump[0] = [4, 6]

        dp = [1] * 10
        for _ in range(n - 1):
            new_dp = [0] * 10
            for i in range(10):
                new_dp[i] = sum(dp[nxt] for nxt in cell2jump[i])

            dp = new_dp

        return sum(dp) % (10**9 + 7)
