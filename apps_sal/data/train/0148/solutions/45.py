class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        def binary_search(arr, target):
            l, r = 0, len(arr) - 1
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][0] <= target:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        jobs = sorted([d, p] for d, p in zip(difficulty, profit))
        for i in range(1, len(jobs)):
            jobs[i][1] = max(jobs[i][1], jobs[i - 1][1])
        res = 0
        for w in worker:
            i = binary_search(jobs, w)
            if i == -1:
                continue
            res += jobs[i][1]
        return res
