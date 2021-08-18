from collections import deque


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        arr.append(-1)
        decrease = []
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                decrease.append(i)
        if len(decrease) == 0:
            return 0
        start = decrease[0] + 1
        end = decrease[-1]

        def valid(start, end):
            if arr[start - 1] <= arr[end + 1]:
                return True
            return False
        res = n - 1
        for i in range(start, -1, -1):
            lo, hi = end, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if valid(i, mid):
                    hi = mid - 1
                else:
                    lo = mid + 1
            lo = min(lo, n - 1)
            res = min(res, lo - i + 1)
        return res
