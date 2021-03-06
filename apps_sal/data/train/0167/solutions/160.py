class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(1, N + 1))
        for _ in range(K - 1):
            temp = [1]
            for j in range(1, N):
                temp.append(temp[-1] + dp[j - 1] + 1)
            dp = temp
        return [i + 1 for (i, x) in enumerate(dp) if x >= N][0]
