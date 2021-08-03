class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[0, 0]] + sorted([[difficulty[i], profit[i]] for i in range(len(profit))])
        for i in range(1, len(jobs)):
            jobs[i][1] = max(jobs[i - 1][1], jobs[i][1])
        res, workerCounts = 0, collections.Counter(worker)

        def binarySearch(n):
            l, r = 0, len(jobs) - 1
            while l < r - 1:

                mid = (l + r) // 2
                if jobs[mid][0] > n:
                    r = mid - 1
                else:
                    l = mid
            return jobs[l][1] if jobs[r][0] > n else jobs[r][1]

        for work, count in list(workerCounts.items()):
            res += binarySearch(work) * count
        return res
