class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # base case for only 1 egg
        dp = list(range(N + 1))
        for k in range(1, K):
            newdp = [0]
            opt = 1
            for n in range(1, N + 1):
                # the optimum choice (intersection of two values) increases with n
                tmp = max(dp[opt - 1], newdp[n - opt])
                while opt < n and tmp > max(dp[opt], newdp[n - opt - 1]):
                    tmp = max(dp[opt], newdp[n - opt - 1])
                    opt += 1
                newdp.append(1 + tmp)
            dp = newdp
        return dp[-1]
