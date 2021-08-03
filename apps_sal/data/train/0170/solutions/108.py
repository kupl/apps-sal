class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        left, right = 0, n - 1
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        res = min(n - left - 1, right)
        j = right
        for i in range(left + 1):
            while j <= n - 1 and arr[i] > arr[j]:
                j += 1
            if j <= n - 1:
                res = min(res, j - i - 1)
        return res
