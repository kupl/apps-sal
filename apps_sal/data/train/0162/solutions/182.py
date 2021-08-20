class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = {}
        return self.recursiveLCS(text1, text2, len(text1) - 1, len(text2) - 1)

    def recursiveLCS(self, text1, text2, p1, p2):
        if p1 < 0 or p2 < 0:
            return 0
        if (p1, p2) in self.dp:
            self.dp[p1, p2] = self.dp[p1, p2]
            return self.dp[p1, p2]
        if text1[p1] == text2[p2]:
            self.dp[p1, p2] = 1 + self.recursiveLCS(text1, text2, p1 - 1, p2 - 1)
        else:
            self.dp[p1, p2] = max(self.recursiveLCS(text1, text2, p1 - 1, p2), self.recursiveLCS(text1, text2, p1, p2 - 1))
        return self.dp[p1, p2]
