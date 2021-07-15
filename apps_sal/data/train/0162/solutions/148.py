class Solution:
    
    def lcs(self, i, j):
        if (i, j) not in self.memo:
            if i == len(self.s) or j == len(self.p):
                ans =  0
            elif self.s[i] == self.p[j]:
                ans = self.lcs(i+1, j+1) + 1
            else:
                ans = max(self.lcs(i+1, j), self.lcs(i, j+1))
            self.memo[(i, j)] = ans
        return self.memo[(i, j)]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.s, self.p = text1, text2
        self.memo = {}
        return self.lcs(0, 0)
