class Solution:

    def knightDialer(self, n: int) -> int:
        d = {0: [4, 6], 1: [6, 8], 2: [9, 7], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [6, 2], 8: [3, 1], 9: [4, 2]}
        res = 0
        dp = [1] * 10
        for x in range(1, n):
            temp = [0] * 10
            for i in range(10):
                for j in d[i]:
                    temp[j] += dp[i]
            dp = temp
        res = sum(dp) % (10 ** 9 + 7)
        return res
