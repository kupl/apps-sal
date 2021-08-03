from bisect import bisect_right


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr = [float('-inf')] + arr + [float('inf')]
        if arr == sorted(arr):
            return 0
        N = len(arr)
        negatives = [None, None]
        for i in range(1, N):
            diff = arr[i] - arr[i - 1]
            if diff < 0:
                if negatives[0] is None:
                    negatives[0] = i
                negatives[1] = i
        ans = float('inf')
        for j in range(negatives[1], N):
            idx = bisect_right(arr, arr[j], hi=negatives[0])
            ans = min(ans, j - idx)
        return ans
