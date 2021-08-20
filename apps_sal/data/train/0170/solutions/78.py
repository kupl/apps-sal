from typing import *


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        (i, j) = (0, n - 1)
        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1
        if i == n - 1:
            return 0
        while j > i and arr[j - 1] <= arr[j]:
            j -= 1
        res = min(n - i - 1, j)
        oldi = i
        oldj = j
        i = 0
        while i <= oldi and j < n:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
        return res


print(Solution().findLengthOfShortestSubarray([1, 3, 2, 4]))
print(Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]))
