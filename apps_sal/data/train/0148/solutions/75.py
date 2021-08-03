class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        def bs(arr, s, e, target):
            while s <= e:
                mid = s + (e - s) // 2
                if arr[mid][0] <= target:
                    s = mid + 1
                else:
                    e = mid - 1
            return e

        arr = []
        for pd in sorted(zip(difficulty, profit)):
            if arr and arr[-1][1] >= pd[1]:
                continue
            arr.append(pd)

        res = 0
        N = len(arr)
        for w in worker:
            idx = bs(arr, 0, N - 1, w)
            if idx >= 0:
                res += arr[idx][1]

        return res
