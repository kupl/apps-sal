from sortedcontainers import SortedDict


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        last = -float('inf')
        sl = SortedDict()
        for (i, n) in enumerate(arr):
            if n < last:
                break
            sl[n] = i
            last = n
        ans = len(arr) - i
        last = float('inf')
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > last:
                break
            last = arr[i]
            sl_idx = sl.bisect_right(arr[i])
            ans = min(ans, i - sl_idx)
        return max(0, ans)
