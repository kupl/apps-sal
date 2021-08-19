class Solution:

    def knightDialer(self, N: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 3 for _2 in range(4)]
        for i in range(4):
            for j in range(3):
                if (i, j) in [(3, 0), (3, 2)]:
                    continue
                dp[i][j] = 1
        for k in range(1, N):
            new_dp = [[0] * 3 for _2 in range(4)]
            for i in range(3):
                for j in range(i, 3):
                    a = [[i + 2, j + 1], [i + 2, j - 1], [i - 2, j + 1], [i - 2, j - 1], [i + 1, j + 2], [i - 1, j + 2], [i + 1, j - 2], [i - 1, j - 2]]
                    for p in a:
                        if not 0 <= p[0] < 4 or not 0 <= p[1] < 3:
                            continue
                        new_dp[i][j] += dp[p[0]][p[1]] % MOD
            new_dp[1][0] = new_dp[1][2]
            new_dp[2][0] = new_dp[2][2]
            new_dp[2][1] = new_dp[0][1]
            i = 3
            j = 1
            new_dp[3][1] = (dp[1][2] + dp[1][0]) % MOD
            dp = new_dp
        s = 0
        for i in dp:
            for j in i:
                s += j % MOD
        return s % MOD
