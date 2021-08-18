from collections import defaultdict as ddic


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        dic = ddic(int)
        sum_ = 0
        dic[0] = -1
        L = len(arr)
        dp = [0] * L
        dp2 = [-1] * L
        res = float('inf')
        for i in range(L):
            sum_ += arr[i]
            dic[sum_] = i
            if sum_ - target in dic:
                dp[i] = i - dic[sum_ - target]
                dp2[i] = i - dic[sum_ - target]
                if i != 0:
                    if dp2[i - 1] != -1:
                        dp2[i] = min(dp2[i], dp2[i - 1])

                if dp2[dic[sum_ - target]] != -1:
                    res = min(res, dp[i] + dp2[dic[sum_ - target]])
            if dp2[i] == -1:
                if i != 0:
                    dp2[i] = dp2[i - 1]
        if res > L:
            return -1
        return res
