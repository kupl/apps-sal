from sortedcontainers import SortedList


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        last = -float('inf')
        sl = SortedList()
        for (i, n) in enumerate(arr):
            if n < last:
                break
            sl.add(n)
            last = n
        ans = len(arr) - len(sl)
        last = float('inf')
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > last:
                break
            last = arr[i]
            sl_idx = sl.bisect_right(arr[i])
            ans = min(ans, i - sl_idx)
        return max(0, ans)
