
# 837. New 21 Game

class Solution1:
    def new21Game(self, N: int, K: int, W: int) -> float:

        dp = [None] * (K + W)
        s = 0
        for i in range(K, K + W):          # 填蓝色的格子
            dp[i] = 1 if i <= N else 0
            s += dp[i]
        for i in range(K - 1, -1, -1):      # 填橘黄色格子
            dp[i] = s / W
            s = s - dp[i + W] + dp[i]
        return dp[0]

# 作者：Mcdull0921
# 链接：https://leetcode-cn.com/problems/new-21-game/solution/huan-you-bi-zhe-geng-jian-dan-de-ti-jie-ma-tian-ge/


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [1 if i <= N else 0 for i in range(K + W)]
        s = sum(dp[K: K + W])
        for i in range(K - 1, -1, -1):
            dp[i] = s / W
            s = s - dp[i + W] + dp[i]
        return dp[0]
