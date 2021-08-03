class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r and arr[l] <= arr[l + 1]:
            l += 1
        if l == r:
            return 0

        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1

        min_remove = min(len(arr) - l - 1, r)

        for i in range(l + 1):
            if arr[i] <= arr[r]:
                min_remove = min(min_remove, r - i - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break

        return min_remove
