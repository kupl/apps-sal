class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        for dCand in range(1, d + 1):
            for targetCand in range(1, target + 1):
                if dCand == 1:
                    dp[dCand][targetCand] = 1 if targetCand <= f else 0
                    continue
                allCombos = 0
                for option in range(1, f + 1):
                    allCombos += dp[dCand - 1][max(0, targetCand - option)]
                dp[dCand][targetCand] = allCombos % (10 ** 9 + 7)
        return dp[d][target]
        '\n        dp[d][t]:\n            for each side:\n                smallerAns = dp[d-1][target-side]\n            dp[d][f] = sum of smaller answers\n        \n        base case:\n            dp[1][t] = 1 if t <= f, 0 otherwise\n            dp[d][<=0] = 0\n        '
