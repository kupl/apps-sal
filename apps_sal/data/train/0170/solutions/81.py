class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n):
            if i + 1 >= n or arr[i] > arr[i + 1]:
                l_end = i
                break
        for i in range(n - 1, -1, -1):
            if i - 1 < 0 or arr[i - 1] > arr[i]:
                r_start = i
                break
        if r_start <= l_end:
            return 0
        i, j = 0, r_start
        res = min(n - (l_end + 1), r_start)
        for i in range(l_end + 1):
            while j < n and arr[i] > arr[j]:
                j += 1
            res = min(res, j - i - 1)
        return res
