class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        return self.lcs(text1, 0, text2, 0, memo)

    def lcs(self, t1, i, t2, j, memo):
        if i >= len(t1) or j >= len(t2):
            return 0
        elif memo[i][j] != -1:
            return memo[i][j]
        else:
            result = -1
            if t1[i] == t2[j]:
                result = 1 + self.lcs(t1, i + 1, t2, j + 1, memo)
            else:
                result = max(self.lcs(t1, i + 1, t2, j, memo), self.lcs(t1, i, t2, j + 1, memo))
            memo[i][j] = result
            return result
