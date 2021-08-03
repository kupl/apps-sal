class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        for i in range(n - 1):
            if arr[i + 1] < arr[i]:
                break
        left = i
        for i in range(n - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                break
        right = i
        if right <= left:
            return 0
        i = 0
        j = right
        ans = min(n - left - 1, right)
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            elif arr[j] < arr[i]:
                j += 1
        return n - 1 if ans == n + 1 else ans
