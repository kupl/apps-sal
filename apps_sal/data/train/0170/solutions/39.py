class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if all([arr[i + 1] >= arr[i] for i in range(len(arr) - 1)]):
            return 0
        start = 0
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                start = i
            else:
                break
        end = len(arr) - 1
        for i in range(len(arr) - 1)[::-1]:
            if arr[i] <= arr[i + 1]:
                end = i
            else:
                break
        lo = -1
        res = min(len(arr) - start - 1, end)
        for i in range(end, len(arr)):
            while lo < start and arr[lo + 1] <= arr[i]:
                lo += 1
            res = min(res, i - lo - 1)
        return res
