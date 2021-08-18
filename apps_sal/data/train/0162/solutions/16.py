class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * l2 for i in range(l1)]

        def get(r, c): return 0 if -1 in [r, c] else dp[r][c]

        for r, c1 in enumerate(text1):
            for c, c2 in enumerate(text2):

                if c1 == c2:
                    dp[r][c] = get(r - 1, c - 1) + 1
                else:
                    dp[r][c] = max(get(r - 1, c), get(r, c - 1))

        for i in dp:
            print(i)
        return dp[-1][-1]
