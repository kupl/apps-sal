class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        while left < len(arr) - 1:
            if arr[left] <= arr[left + 1]:
                left += 1
            else:
                break
        if left >= len(arr) - 1:
            return 0
        right = len(arr) - 1
        while right > 0:
            if arr[right] >= arr[right - 1]:
                right -= 1
            else:
                break
        ll = 0
        rr = right
        res = min(len(arr) - left - 1, right)
        while ll < left + 1 and rr < len(arr):
            if arr[ll] <= arr[rr]:
                res = min(res, rr - ll - 1)
                ll += 1
            else:
                rr += 1
        return res
