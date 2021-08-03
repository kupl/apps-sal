class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        self.store = [[-1 for i in range(m)] for j in range(n)]

        self.Rec(text1, text2, n - 1, m - 1)

        return self.store[-1][-1]

    def Rec(self, text1, text2, n, m):

        if(n < 0 or m < 0):
            return 0

        if(self.store[n][m] != -1):
            return self.store[n][m]

        if(text1[n] == text2[m]):

            x = 1 + self.Rec(text1, text2, n - 1, m - 1)

            self.store[n][m] = x

        else:
            x = max(self.Rec(text1, text2, n - 1, m), self.Rec(text1, text2, n, m - 1))

            self.store[n][m] = x

        return x
