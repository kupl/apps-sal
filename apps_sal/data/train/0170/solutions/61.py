class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        (i, j) = (-1, -1)
        L = len(arr)
        for k in range(L - 1):
            if arr[k] > arr[k + 1]:
                j = k + 1
                if i == -1:
                    i = k
        if i == -1:
            return 0
        res = j
        for m in range(i + 1):
            while j <= L - 1:
                if arr[j] >= arr[m]:
                    break
                j += 1
            if j == L:
                return min(res, L - i - 1)
            else:
                res = min(res, j - m - 1)
        return res
