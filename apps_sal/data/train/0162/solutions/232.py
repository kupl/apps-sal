class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0]*(len(text2)+1)
        for i in range(1, len(text1)+1):
            prev = dp[0]
            for j in range(1, len(text2)+1):
                last = dp[j]
                if text1[i-1]==text2[j-1]:
                    dp[j] = prev+1
                if last>prev:
                    prev = last
        return max(dp)
