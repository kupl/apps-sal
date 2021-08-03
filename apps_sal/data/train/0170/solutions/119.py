class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        l = 0
        r = n - 1
        ans = 0

        while l < n - 1 and arr[l] <= arr[l + 1]:
            l += 1
        if l == n - 1:
            return 0

        ans = n - l - 1

        while r >= l and arr[r] >= arr[r - 1]:
            r -= 1

        if r == 0:
            return n - 1
        ans = min(ans, r)
        i = 0
        j = r

        while i <= l and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1

        return ans
