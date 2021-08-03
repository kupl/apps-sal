class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def get_code_len(x):
            return 1 + len(str(x)) if x > 1 else x

        n = len(s)
        dp = [[n] * (k + 1) for i in range(n + 1)]
        dp[0] = [0] * (k + 1)
        for i in range(n):
            for j in range(k + 1):
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])

                deletions = 0
                for p in reversed(range(i + 1)):
                    if s[p] != s[i]:
                        deletions += 1
                    if deletions > j:
                        break
                    dp[i + 1][j - deletions] = min(dp[i + 1][j - deletions],
                                                   dp[p][j] + get_code_len(i - p - deletions + 1))

        return min(dp[n])
