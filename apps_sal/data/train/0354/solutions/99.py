class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dynamic programming
        # dp[i][j][k] # at pos i, we end with j, and the number of continuous of j at the end is k

        dp = [[[0 for k in range(rollMax[j] + 1)] for j in range(6)] for _ in range(n)]

        for j in range(6):
            dp[0][j][1] = 1

        for i in range(n):
            for j in range(6):
                for k in range(2, rollMax[j] + 1):  # 这里 原则上来说应该写成 range(2)开始，因为 k-1>=1,但是写成 1也没有关系，因为 k-1=0, += 0, 没有影响。
                    dp[i][j][k] += dp[i - 1][j][k - 1]

                for otherj in range(6):
                    if otherj != j:
                        for k in range(1, rollMax[otherj] + 1):
                            dp[i][j][1] += dp[i - 1][otherj][k]
        # print(\"dp=\", dp)
        return sum([sum(x) % (10**9 + 7) for x in dp[-1]]) % (10**9 + 7)
# 题解，这种计算个数的一般都是动态规划。注意到题目中 rollMax[i] >=1说明 只要上一个不一样，那么我这次出那个数字都是可以的。最后别忘了求 mod
# 动态规划， 最重要的是，要记录哪种状态。这里 要求的是 某个 number 不能连续超过 rollMax[j]次，那么显然我们需要记录这件事。然后当前的位置需要记录，最后一个数字是什么需要记录，最后一个数字出现多少次，需要记录，于是三维 dp 出现了。

# dp[i][j][k] 代表 到第 i 个位置时，以数字 j 结尾，结尾处 连续出现 k 次。 那么其实这里就要求 k >= 1 的，因为以 j结尾了，那么肯定至少有一个数字了。
# dp 三维数组的维度怎么确定呢？ i，j 是很显然，一个是 n，一个是6，那么k维度，我们用 roolMax[j] + 1 这个维度，因为 我们出现的个数 0，1，2，3，4，。。。，一直到 roolMax[j] 都是可以的，所以 range （roolMax[j] + 1).
# 那么 j 用 range(6) = 0, 1, 2, 3, 4,5 这里是没有关系的，正好和 roolMax[j] 的 index 对应起来。 不用 换成 1，2，3，4，5，6.
