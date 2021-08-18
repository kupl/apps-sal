class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        longest_array = 0
        while l < len(arr) - 1 and arr[l + 1] >= arr[l]:
            l += 1
        longest_array = l + 1

        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        longest_array = max(longest_array, len(arr) - r)

        p1 = 0
        p2 = r

        while p1 <= l and p2 < len(arr):
            if arr[p1] <= arr[p2]:
                longest_array = max(longest_array, p1 + len(arr) - p2 + 1)
                p1 += 1
            else:
                p2 += 1

        if len(arr) - longest_array < 0:
            return 0

        return len(arr) - longest_array
