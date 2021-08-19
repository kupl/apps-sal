# https://zxi.mytechroad.com/blog/searching/leetcode-996-number-of-squareful-arrays/
# g[i][j]: if i and j are squareful
# dp[s][i]: # of ways to reach state s (binary mask of nodes visited) that ends with node i
# dp[s | (1 << j)][j] += dp[s][i] if g[i][j]
# 先对数组排序, 然后计算出所有的 g[i][j]
# for i in range(n) 初始化 dp[(1 << i)][i] = 1, 表示只有一个数字 i 的情况, 每个都是一种
# 如果有多个重复的数字, 只用第一个数字作为开头
# ans = sum(dp[(1 << n) - 1][i])
# O(n^2*2^n) time complexity, O(2^n) space complexity
import math


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        A = sorted(A)
        g = [[False] * n for _ in range(n)]
        dp = [[0] * n for _ in range(1 << n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if int((A[i] + A[j]) ** 0.5 + 0.5) ** 2 == A[i] + A[j]:
                    g[i][j] = True

        for i in range(n):
            if i > 0 and A[i] == A[i - 1]:  # For the same numbers, only the first one can be the starting point
                continue
            dp[1 << i][i] = 1

        for s in range(1 << n):
            for i in range(n):
                if dp[s][i] <= 0:  # 如果 dp[s][i] <= 0, 说明没有以 i 结尾的情况, 跳过
                    continue
                for j in range(n):  # 尝试让任意一个数字连接在最后面
                    if not g[i][j] or (s & (1 << j)):  # 如果 i, j 不是 squareful 或 j 已经使用过, 跳过
                        continue
                    if j > 0 and not (s & (1 << (j - 1))) and A[j] == A[j - 1]:  # 出现重复的只使用第一个
                        continue
                    dp[s | (1 << j)][j] += dp[s][i]

        res = 0
        for i in range(n):
            res += dp[(1 << n) - 1][i]
        return res
