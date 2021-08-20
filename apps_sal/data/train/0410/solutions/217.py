dp = {}


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        result = [(num, self.getPowerValue(num)) for num in range(lo, hi + 1)]
        result.sort(key=lambda x: (x[1], x[0]))
        return result[k - 1][0]

    def getPowerValue(self, num) -> int:
        if num == 1:
            return 0
        if num in dp:
            return dp[num]
        if num % 2 == 0:
            dp[num] = 1 + self.getPowerValue(num / 2)
        else:
            dp[num] = 1 + self.getPowerValue(3 * num + 1)
        return dp[num]
