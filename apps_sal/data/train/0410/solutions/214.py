class Solution:

    def __recur(self, dp, num):
        if num in dp:
            return dp[num]
        res = 0
        if num % 2 == 0:
            res = self.__recur(dp, int(num / 2)) + 1
        else:
            res = self.__recur(dp, int(num * 3) + 1) + 1
        dp[num] = res
        return res

    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {1: 0}
        for i in range(1, 1001):
            self.__recur(dp, i)
        power_order = sorted([(dp[key], key) for key in dp if key >= lo and key <= hi])
        return power_order[k - 1][1]
