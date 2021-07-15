class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = [[0] * len(text2) for _ in range(len(text1))]
        
        if text1[0] == text2[0]:
            m[0][0] = 1
        
        for i in range(1, len(text1)):
            m[i][0] = 1 if text1[i] == text2[0] else m[i-1][0]
        for i in range(1, len(text2)):
            m[0][i] = 1 if text2[i] == text1[0] else m[0][i-1]
            
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    m[i][j] = max(1 + m[i - 1][j - 1], m[i - 1][j], m[i][j - 1])
                else:
                    m[i][j] = max(m[i - 1][j], m[i][j - 1])
        return m[-1][-1]
