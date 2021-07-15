class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.n = len(text1)
        self.m = len(text2)
        self.text1 = text1
        self.text2 = text2
        self.table = []
        for i in range(self.n):
            self.table.append([-1] * self.m)
        return self.longest(0,0)
            
    def longest(self, i, j):
        if (i == self.n) or (j == self.m):
            return 0
        if self.table[i][j] != -1:
            return self.table[i][j]
        else:
            if self.text1[i] == self.text2[j]:
                self.table[i][j] = 1 + self.longest(i+1, j+1)
            else:
                self.table[i][j] = max(self.longest(i+1, j), self.longest(i, j+1))
            return self.table[i][j]
            

