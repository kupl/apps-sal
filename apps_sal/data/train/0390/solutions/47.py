class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # 每次移除平方数
        # alice每次移除完不能剩余平方数，否则就输
        # 当前数字减去一个平方数后，不能是平方数
        # 从小到大计算，n=1，。。。，n
        # dp[i]: 有i个石头时，alice能不能赢
        # dp[i] = 从i向下减去平方数，对应的dp[j]有一个是false即可
        dp = [False for _ in range(n + 1)]
        for i in range(1, n + 1):
            base = 1
            while i - base**2 >= 0:
                if not dp[i - base**2]:
                    dp[i] = True
                    break
                else:
                    base += 1
            if i < n and ((n - i)**0.5) % 1 == 0 and not dp[i]:
                return True
        return dp[n]
