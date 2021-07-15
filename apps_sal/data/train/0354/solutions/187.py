def simulatorHelper(n, rollMax, consec, rolls, last, dp):
    if rolls == n:
        return 1
    elif dp[rollMax[last]][consec][rolls] != -1:
        return dp[rollMax[last]][consec][rolls]
    else:
        total = 0
        for i in range(len(rollMax)):
            if last == i and consec == rollMax[i]:
                continue
            else:
                if last == i:
                    total += simulatorHelper(n, rollMax, consec + 1, rolls + 1, i, dp)
                else:
                    total += simulatorHelper(n, rollMax, 1, rolls + 1, i, dp)
        dp[rollMax[last]][consec][rolls] = total
        return total
def simulator(n, rollMax):
    dp = [[[-1 for rolls in range(n + 1)] for consec in range(16)] for rollMax in range(16)]
    return simulatorHelper(n, rollMax, 0, 0, 0, dp) % (10 ** 9 + 7)

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        return simulator(n, rollMax)
