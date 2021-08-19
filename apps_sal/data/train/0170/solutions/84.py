import bisect


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        (start, end) = (0, len(arr) - 1)
        while start < len(arr) - 1:
            if arr[start] > arr[start + 1]:
                break
            start += 1
        if start == len(arr) - 1:
            return 0
        while end > 0:
            if arr[end] < arr[end - 1]:
                break
            end -= 1
        best_dist = end
        for i in range(start, -1, -1):
            j = bisect.bisect_left(arr, arr[i], end, len(arr))
            dist = j - i - 1
            best_dist = min(best_dist, dist)
        return best_dist
