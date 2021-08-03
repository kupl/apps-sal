class Solution:
    def longestCommonSubsequence1(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper(s1, s2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):
        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
            else:
                memo[i][j] = max(
                    self.helper(s1, s2, i + 1, j, memo),
                    self.helper(s1, s2, i, j + 1, memo),
                )
        return memo[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i1, i2):
            if (i1, i2) in self.memo:
                return self.memo[(i1, i2)]

            res = 0
            if i1 == len(text1) or i2 == len(text2):
                res = 0
            elif text1[i1] == text2[i2]:
                res = 1 + helper(i1 + 1, i2 + 1)
            else:
                res = max(helper(i1 + 1, i2), helper(i1, i2 + 1))

            self.memo[(i1, i2)] = res
            return self.memo[(i1, i2)]

        self.memo = {}
        return helper(0, 0)
