class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1

        dp = [0]
        cur, temp = 1, 1 / W
        for i in range(1, W + 1):
            dp.append(cur / W)
            if i < K:
                cur += dp[-1]

        # print(dp)
        total = sum(dp[1:min(W + 1, K)])
        left = 1
        for i in range(W + 1, W + K):
            dp.append(total / W)
            total -= dp[left]
            left += 1
            if i < K:
                total += dp[-1]
        # print(dp)
        end = sum(dp[K:])
        good_end = sum(dp[K:N + 1])
        return good_end / end
