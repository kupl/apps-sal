class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        (l, r) = (0, n - 1)
        while l < n - 1 and arr[l] <= arr[l + 1]:
            l += 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        nums_to_rm = min(n - 1 - l, r)
        for c in range(l + 1):
            if arr[c] <= arr[r]:
                nums_to_rm = min(nums_to_rm, max(0, r - c - 1))
            elif r < n - 1:
                r += 1
            else:
                break
        return nums_to_rm
