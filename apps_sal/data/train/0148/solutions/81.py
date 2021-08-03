class Solution:
    def binarySearch(self, l, r, x, li):
        if (r - l <= 1):
            if (li[r] <= x):
                return r
            else:
                return l
        m = (l + r + 1) // 2
        if (li[m] <= x):
            return self.binarySearch(m, r, x, li)
        else:
            return self.binarySearch(l, m - 1, x, li)

    def maxProfitAssignment(self, difficulty, profit, worker):
        difficulty.append(0)
        profit.append(0)
        jobs = sorted(zip(difficulty, profit))
        J = len(jobs)
        jobDifficulty = [j[0] for j in jobs]
        mostProfit = [jobs[0][1] for j in jobs]
        for i in range(1, J):
            mostProfit[i] = max(jobs[i][1], mostProfit[i - 1])
        totProfit = 0
        for w in worker:
            maxJob = self.binarySearch(0, J - 1, w, jobDifficulty)
            totProfit += mostProfit[maxJob]
        return totProfit
