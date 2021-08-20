class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        (left, right) = (1, n - 1)
        while left < n and arr[left] >= arr[left - 1]:
            left += 1
        if left == n:
            return 0
        while left < right and arr[right] >= arr[right - 1]:
            right -= 1
        res = min(n - left, right)
        left -= 1
        while left >= 0:
            (l, r) = (right - 1, n - 1)
            while r - l > 1:
                m = (l + r) // 2
                if arr[m] >= arr[left]:
                    r = m
                else:
                    l = m
            if arr[left] > arr[r]:
                r += 1
            res = min(res, r - left - 1)
            left -= 1
        return res
