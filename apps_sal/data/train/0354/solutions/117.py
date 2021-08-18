class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        maxRolls = min(n, max(rollMax))
        dp = [[[0] * (maxRolls + 1) for _ in range(7)] for _ in range(2)]

        for j in range(1, 7):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            iMod2 = i % 2
            iMinus1Mod2 = (i - 1) % 2

            for j in range(1, 7):
                dp[iMod2][j][1] = 0
                for jj in range(1, 7):
                    if jj == j:
                        continue
                    for kk in range(1, min(i - 1, rollMax[jj - 1]) + 1):
                        dp[iMod2][j][1] = sumMod(dp[iMod2][j][1], dp[iMinus1Mod2][jj][kk])

                for k in range(2, min(i, rollMax[j - 1]) + 1):
                    dp[iMod2][j][k] = dp[iMinus1Mod2][j][k - 1]

        result = 0
        nMod2 = n % 2
        for j in range(1, 7):
            for k in range(1, min(n, rollMax[j - 1]) + 1):
                result = sumMod(result, dp[nMod2][j][k])

        return result


def sumMod(x: int, y: int) -> int:
    return (x + y) % (10 ** 9 + 7)
