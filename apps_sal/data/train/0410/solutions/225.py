class Solution:

    def power(self, memo, num):
        if num in memo:
            return memo[num]
        result = 0
        if num % 2 == 0:
            result = self.power(memo, num // 2) + 1
        else:
            result = self.power(memo, num * 3 + 1) + 1
        memo[num] = result
        return result

    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}
        for num in range(1, 1001):
            self.power(memo, num)
        porder = sorted([(memo[key], key) for key in memo if key >= lo and key <= hi])
        return porder[k - 1][1]
