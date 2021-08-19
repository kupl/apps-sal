class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # find the first inst in left side where arr[i] < arr[i-1]
        # next, find the first inst in right side where arr[j] < arr[j-1]
        # next, we start i from 0, j at j
        # we shrink window if arr[i] <= arr[j]
        # we expand window if arr[i] > arr[j]
        # we store the size of the window to ans
        n = len(arr)
        left = 0
        while (left + 1 < n and arr[left] <= arr[left + 1]):
            left += 1
        if left == n - 1:
            return 0

        right = n - 1
        while (right > left and arr[right - 1] <= arr[right]):
            right -= 1

        ans = min(n - left - 1, right)
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
        return ans
