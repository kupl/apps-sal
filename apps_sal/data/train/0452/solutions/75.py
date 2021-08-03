class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = {}
        myIntMax = 10000000

        def findMinDif(jobIdx, daysLeft):
            if daysLeft < 0:
                return -1
            if jobIdx == n and daysLeft > 0:
                return -1
            if jobIdx == n and daysLeft == 0:
                return 0

            if str(jobIdx) + str(daysLeft) in dp:
                return dp[str(jobIdx) + str(daysLeft)]

            todayDiff = 0
            totalDiff = myIntMax

            for idx in range(jobIdx, n):
                todayDiff = max(todayDiff, jobDifficulty[idx])
                nextDiff = findMinDif(idx + 1, daysLeft - 1)
                dp[str(idx + 1) + str(daysLeft - 1)] = nextDiff

                if nextDiff != -1:
                    totalDiff = min(totalDiff, todayDiff + nextDiff)
                else:
                    break

            return totalDiff

        ret = findMinDif(0, d)
        if ret == myIntMax:
            return -1
        else:
            return ret
