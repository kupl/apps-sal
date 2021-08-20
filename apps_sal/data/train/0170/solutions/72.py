class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left + 1 <= len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == right:
            return 0
        while right - 1 >= 0 and arr[right] >= arr[right - 1]:
            right -= 1
        min_sublen = min(right, len(arr) - 1 - left)
        lp = 0
        rp = right
        while lp <= left and rp <= len(arr) - 1:
            if arr[lp] > arr[rp]:
                rp += 1
            else:
                min_sublen = min(min_sublen, rp - lp - 1)
                lp += 1
        return min_sublen
