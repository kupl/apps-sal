import sys


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        table = {0: -1}
        cursum = 0
        dp1 = [sys.maxsize for i in range(len(arr))]

        for i in range(len(arr)):
            if i > 0:
                dp1[i] = dp1[i - 1]
            cursum += arr[i]
            if cursum - target in list(table.keys()):
                dp1[i] = min(dp1[i], i - table[cursum - target])
            table[cursum] = i

        table = {0: len(arr)}
        cursum = 0
        dp2 = [sys.maxsize for i in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            if i < len(arr) - 1:
                dp2[i] = dp2[i + 1]
            cursum += arr[i]
            if cursum - target in list(table.keys()):
                dp2[i] = min(dp2[i], table[cursum - target] - i)
            table[cursum] = i

        res = sys.maxsize

        for i in range(len(dp1) - 1):
            if dp1[i] != sys.maxsize and dp2[i + 1] != sys.maxsize:
                res = min(res, dp1[i] + dp2[i + 1])

        if res == sys.maxsize:
            return -1
        else:
            return res
