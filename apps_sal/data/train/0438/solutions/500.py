import collections


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dic = {}
        n = len(arr)
        for i in range(1, n + 1):
            dic[i] = (-1, -1, 0)
        res = -1
        memo = collections.defaultdict(int)
        for i in range(n):
            left = arr[i]
            right = arr[i]
            l = 1
            if arr[i] + 1 <= n and dic[arr[i] + 1][2] != 0:
                right = dic[arr[i] + 1][1]
                l += dic[arr[i] + 1][2]
                memo[dic[arr[i] + 1][2]] -= 1

            if arr[i] - 1 >= 1 and dic[arr[i] - 1][2] != 0:
                left = dic[arr[i] - 1][0]
                l += dic[arr[i] - 1][2]
                memo[dic[arr[i] - 1][2]] -= 1

            for x in [left, right]:
                dic[x] = (left, right, l)
            memo[l] += 1
            if memo[m] > 0:
                res = i + 1

        return res
