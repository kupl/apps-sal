class Solution:

    def recursiveLCS(self, t1, t2):
        if not t1 or not t2:
            return 0
        elif t1[0] == t2[0]:
            return 1 + self.recursiveLCS(t1[1:], t2[1:])
        else:
            left = self.recursiveLCS(t1[1:], t2)
            right = self.recursiveLCS(t1, t2[1:])
            return max(left, right)

    def recursiveLongestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.recursiveLCS(text1, text2)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        DP = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    DP[i][j] = 1 + DP[i - 1][j - 1]
                else:
                    left = DP[i - 1][j]
                    right = DP[i][j - 1]
                    DP[i][j] = max(left, right)
        for row in DP:
            print(row)
        return DP[len(text1)][len(text2)]
