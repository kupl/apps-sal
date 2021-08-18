class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        i, j = 0, n - 1
        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1
        if i == n - 1:
            return 0
        while j > 0 and arr[j] >= arr[j - 1]:
            j -= 1
        if j == 0:
            return n - 1

        res = min(n - 1 - i, j)

        for k in range(i + 1):
            if arr[k] <= arr[j]:
                res = min(res, j - k - 1)
            elif j < n - 1:
                j += 1
            else:
                break
        return res
