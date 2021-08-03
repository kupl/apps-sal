class Solution:

    def stoneGame(self, piles):

        n = len(piles)
        memo = dict()

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            ans = max(piles[i] - dp(i + 1, j), piles[j] - dp(i, j - 1))
            memo[(i, j)] = ans
            return ans
        return dp(0, n - 1) > 0

    def stoneGame1(self, piles):
        # three methods, dp, memo+recursive
        n = len(piles)

        memo = dict()

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if (j - i + n) % 2 == 1:  # player 1
                ans = max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                ans = min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))
            memo[(i, j)] = ans
            return ans
        return dp(0, n - 1) > 0  # 相对分数

    def stoneGame2(self, piles):
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for alen in range(2, n + 1):
            for i in range(0, n - alen + 1):  # when i=n-alen, alen=n
                j = i + alen - 1  # j - i + 1 = alen, so j = i-1+alen
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0  # 相对分数

    def stoneGame3(self, piles):  # 记忆化递归的方法！相对比较容易写出来
        n = len(piles)
        memo = dict()

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            ans = max(piles[i] - dp(i + 1, j), piles[j] - dp(i, j - 1))  # min-max过程
            memo[(i, j)] = ans
            return ans
        return dp(0, n - 1) > 0  # 相对分数，也就是 score(alex) - score(lee)

    def stoneGame4(self, piles):
        return True

    def stoneGame3(self, piles):
        n = len(piles)
        # dp[i] = max(your stones - op_stones) for piles[i] to piles[i+alen-1] i+alen-1-i+1 = alen = length of piles
        dp = [0] * n
        for alen in range(2, n + 1):
            for i in range(0, n - alen + 1):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + alen - 1] - dp[i])  # 问题，二维转一维的技巧是什么？
        return dp[0] > 0

    def stoneGame2(self, piles):
        # dp[i][j] = max(yourscore - op_stones) for piles[i] ~ piles[j]
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        for alen in range(2, n + 1):  # 长度为从2到n，构造
            for i in range(0, n - alen + 1):  # i这个子问题的范围
                j = i + alen - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
                # j = i + alen - 1 代入
                # dp[i][j] = max(piles[i] - dp[i+1][j], piles[i+alen-1] - dp[i][j-1])
                # 然后直接把j去掉:
                # dp[i] = max(piles[i] - dp[i+1], piles[i+alen-1] - dp[i]) 就是1D的写法。。。
        return dp[0][n - 1] > 0

    def stoneGame1(self, piles: List[int]) -> bool:
        # minmax + dp 或者记忆化递归
        # 你和对手都是选择“最佳”的option来选择

        # 第一种解法：minmax
        # def score(s, l, r)
        #    if l>r: return 0
        #    return max(s[l] - score(s, l+1, r), # left
        #               s[r] - score(s, l, r-1)) # right
        #    对手的最大值，自己的最小值下的 最大值
        #    return score(s, 0, n-1) > 0
        # time: O(2^n), space O(n)

        # 第二种解法：minmax + memorization / DP
        # dp[i][j] = best relative score of subarray s[i] ~ s[j]
        # time O(n^2), space (O^2) -> O(n)

        # solution 1, recursive, 不记忆中间结果，无法达到最优解！O(2^n) 记忆化递归，容易java的stack爆掉。。。
        dp = dict()

        def score(piles, l, r):
            # left, right
            if (l, r) in dp:
                return dp[(l, r)]
            if l == r:
                dp[(l, r)] = piles[l]  # 只剩下一堆的话，就取它了，没有其他可以选择的了！
                return piles[l]
            res = max(piles[l] - score(piles, l + 1, r), piles[r] - score(piles, l, r - 1))
            # 我，当前有两种选择，拿l或者拿r，如果拿l，则得分为piles[l]，失分为对手从l+1,r的区间能得到的最大值（对手的最大值，就是我的最小值）
            # 如果拿r，则得分为piles[r]，失分为对手从l, r-1的区间能得到的最大值（对手的最大值，就是我的最小值）
            # 所以这个过程就是经典的minmax过程
            dp[(l, r)] = res
            return res

        res = score(piles, 0, len(piles) - 1)
        return True if res > 0 else False
