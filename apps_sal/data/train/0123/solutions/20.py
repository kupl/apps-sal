class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        # N = 10   L = 25    K = 4
        # 1~10         24        3
        # 2~9          23        2
        #  Unique : L - N + 1       Extra : N-K+1

        dp = [1] * (L - N + 1)

        for p in range(2, N - K + 1):
            for i in range(1, L - N + 1):
                dp[i] += p * dp[i - 1]

        ans = dp[-1]
        for k in range(2, N + 1):
            ans = ans * k
        return ans % (10**9 + 7)

        dp = [1] * (L - N + 1)
        print(dp)
        for p in range(2, N - K + 1):
            for i in range(1, L - N + 1):

                dp[i] += dp[i - 1] * p
                print((p, i, dp))
        # Multiply by N!
        ans = dp[-1]
        for k in range(2, N + 1):
            ans *= k
        return ans % (10**9 + 7)
