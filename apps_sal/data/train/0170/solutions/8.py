class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        n = len(arr)
        while l < n - 1 and arr[l] <= arr[l + 1]:
            l += 1
        if l == n - 1:
            return 0
        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r - 1]:
            r -= 1
        left = n - (l + 1)
        right = r
        ans = min(left, right)
        i = 0
        j = r
        while i <= l and j < n:
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans
