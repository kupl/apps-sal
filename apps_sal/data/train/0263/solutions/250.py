class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        ret = 0
        dp = [[0] * 10 for i in range(n)]
        for i in range(10):
            dp[0][i] = 1
        graph = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        for i in range(1, n):
            for j in range(10):
                for neighbor in graph[j]:
                    dp[i][j] += dp[i - 1][neighbor]
        ret = sum(dp[n - 1][i] for i in range(10))
        return ret % (10**9 + 7)
# 1 dp需要二维的来表示才行，一维的话，值很容易被覆盖，比如dp[1]在第二步的时候更新了，但是后面又用到dp[1]的话，就会用这个更新的值，而不是第一步的dp值
# 1 这里我开始写成10^9+7了，^在python里是异或呀，幂要写成**
# https://www.jianshu.com/p/5a588aab3ae5
