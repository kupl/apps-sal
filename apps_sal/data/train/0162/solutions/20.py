class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return self.helper(text1, text2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):
        if memo[i][j] != -1:
            return memo[i][j]
        if i == len(s1) or j == len(s2):
            return 0
        ans = 0
        if s1[i] == s2[j]:
            ans = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
        else:
            ans = max(self.helper(s1, s2, i + 1, j, memo), self.helper(s1, s2, i, j + 1, memo))
        memo[i][j] = ans
        return ans
