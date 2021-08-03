class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        # state: dp[k][m]. 如果有K个鸡蛋，最多能抛m次，那么最多可以确定的F最高为几层楼
        # transfer: 如果在某一层楼丢鸡蛋，要不就是碎了，要不就是没碎。
        # 碎了：说明得测楼下： dp[k-1][m-1]为最多能测落下的层数
        # 没碎：说明得测楼上： dp[k][m-1]为最多能测楼上的层数
        # 不管碎还是没碎，总共能测的层数= 楼下 + 楼上 + 1（现在那一层）
        #### dp[k][m] = dp[k-1][m-1] + dp[k][m-1] + 1
        # 每当有一个m值的时候，我们也要从k=1 到k=K去simulate，去填充dp里面的值（dp来自上面和左上角）

        # init: base case是什么呢？比如K=0的时候，肯定测0层。 m=0的时候，也测0层
        #### dp[0][...] = 0; dp[...][0] = 0

        # result: 当dp[K][m] == N 的时候，m就是我们想要的答案. K是大写K，因为我们一开始就有K个鸡蛋

        dp = [[0] * (N + 1) for i in range(K + 1)]

        m = 0
        while dp[K][m] < N:
            m += 1

            for i in range(1, K + 1):
                dp[i][m] = dp[i][m - 1] + dp[i - 1][m - 1] + 1

        return m
