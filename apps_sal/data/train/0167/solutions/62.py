class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        dp = range(N + 1)

        for k in range(2, K + 1):
            dp2 = [0]
            A = 1

            for n in range(1, N + 1):
                costA = max(dp[A - 1], dp2[n - A])
                while A < n:
                    B = A + 1
                    costB = max(dp[B - 1], dp2[n - B])
                    if costB > costA:
                        break
                    costA = costB
                    A += 1
                dp2.append(1 + costA)
            dp = dp2

        return dp[-1]
