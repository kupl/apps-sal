class Solution:
    def knightDialer(self, n: int) -> int:
        # DP 每次要加上那个格的DP值
        #{4, 6}, {6, 8}, {7, 9}, {4, 8}, {3, 9, 0}, {}, {1, 7, 0}, {2, 6}, {1, 9}, {4, 2}
        # 二维数组 表示第i次跳到j上有多少种方法
        # 比如到4的时候 那么可能是从3,9,0 来的 那么i,4 = i,4 + i-1 (3,9,0)
        stack = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,9],[4,2]]
        dp = [[0 for _ in range(10)] for __ in range(n)]
        for i in range(10):
            dp[0][i] = 1
        for i in range(1,n):
            for j in range(10):
                for k in stack[j]:
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % (10**9 + 7)
        return sum(dp[-1][i] for i in range(10))  % (10**9 + 7)
