class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        l, r = n, -1

        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                l = i
                break
        if l == n:
            return 0

        for j in range(n - 2, -1, -1):
            if arr[j] > arr[j + 1]:
                r = j
                break

        ans = min(r + 1, n - l)

        i = 0
        for j in range(r + 1, n):
            while i < l and arr[i] <= arr[j]:
                i += 1
            ans = min(ans, j - i)
        return ans
