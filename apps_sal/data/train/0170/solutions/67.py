class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = n - 1, 0
        for i in range(n):
            if i > 0 and arr[i] < arr[i - 1]:
                left = i - 1
                break
        for i in range(n - 1, -1, -1):
            if i < n - 1 and arr[i] > arr[i + 1]:
                right = i + 1
                break
        if left >= right:
            return 0

        ans = min(n - left, right)
        j = right
        for i in range(left + 1):
            if j < len(arr) and arr[j] < arr[i]:
                j += 1
            ans = min(ans, j - i - 1)
        return ans
