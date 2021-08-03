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
                    allCombos %= (10 ** 9 + 7)
                dp[dCand][targetCand] = allCombos
        return dp[d][target]

        '''
        dp[d][t]:
            for each side:
                smallerAns = dp[d-1][target-side]
            dp[d][f] = sum of smaller answers
        
        base case:
            dp[1][t] = 1 if t <= f, 0 otherwise
            dp[d][<=0] = 0
        '''
