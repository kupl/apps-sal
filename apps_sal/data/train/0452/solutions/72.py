class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        mem = {}
        maxMem = {}
        sumMem = []
        for i, diff in enumerate(jobDifficulty):
            if i == 0:
                sumMem.append(diff)
            else:
                sumMem.append(sumMem[-1] + diff)

        def maxHelper(i, j):
            if (i, j) in maxMem:
                return maxMem[(i, j)]

            maxVal = 0
            for index in range(i, j):
                if jobDifficulty[index] > maxVal:
                    maxVal = jobDifficulty[index]
            maxMem[(i, j)] = maxVal
            return maxVal

        def helper(jobNum, days):
            if (jobNum, days) in mem:
                return mem[(jobNum, days)]

            if jobNum < days:
                return float('inf')

            elif jobNum == days:
                minCplx = sumMem[jobNum - 1]

            elif days == 1:
                minCplx = maxHelper(0, jobNum)

            else:
                minCplx = float('inf')
                for i in range(days - 1, jobNum):
                    curCplx = helper(i, days - 1) + maxHelper(i, jobNum)
                    if curCplx < minCplx:
                        minCplx = curCplx

            mem[(jobNum, days)] = minCplx
            return minCplx

        res = helper(len(jobDifficulty), d)
        return -1 if res == float('inf') else res
