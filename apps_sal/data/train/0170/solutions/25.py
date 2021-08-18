class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)

        lo, hi = 0, N - 1
        while lo + 1 < N and arr[lo] <= arr[lo + 1]:
            lo += 1
        if lo >= N - 1:
            return 0

        while hi - 1 >= 0 and arr[hi - 1] <= arr[hi]:
            hi -= 1

        res = min(N - lo - 1, hi)
        j = hi
        for i in range(lo + 1):
            while j < N and arr[j] < arr[i]:
                j += 1
            res = min(res, j - i - 1)
        return res
