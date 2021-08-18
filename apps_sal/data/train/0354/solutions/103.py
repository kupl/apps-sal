class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        maxRolls = min(n, max(rollMax))
        dp = [[[0] * (maxRolls + 1) for _ in range(7)] for _ in range(n + 1)]

        for j in range(1, 7):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(1, 7):
                for k in range(1, min(i, rollMax[j - 1]) + 1):
                    if k > 1:
                        dp[i][j][k] = sumMod(dp[i][j][k], dp[i - 1][j][k - 1])
                        continue

                    for jj in range(1, 7):
                        if jj == j:
                            continue

                        for kk in range(1, min(i - 1, rollMax[jj - 1]) + 1):
                            dp[i][j][k] = sumMod(dp[i][j][k], dp[i - 1][jj][kk])

        result = 0
        for j in range(1, 7):
            for k in range(1, min(n, rollMax[j - 1]) + 1):
                result = sumMod(result, dp[n][j][k])

        return result


def sumMod(x: int, y: int) -> int:
    return (x + y) % (10 ** 9 + 7)
