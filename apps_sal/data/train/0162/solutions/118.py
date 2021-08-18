class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def helper(i, j):
            if (i, j) in self.h:
                return self.h[i, j]

            if i == n1 or j == n2:
                self.h[i, j] = 0
                return 0

            if text1[i] == text2[j]:
                self.h[i, j] = helper(i + 1, j + 1) + 1
            else:
                self.h[i, j] = max(helper(i + 1, j), helper(i, j + 1))

            return self.h[i, j]

        n1 = len(text1)
        n2 = len(text2)

        self.h = {}

        res = helper(0, 0)

        return res
