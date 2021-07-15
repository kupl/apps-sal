class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mp = {}
        def lcs(i, j):
            if i>=len(text1) or j >=len(text2):
                return 0
            elif (i,j) in mp:
                return mp[(i,j)]
            else:
                if text1[i] == text2[j]:
                    mp[(i,j)] = 1+ lcs(i+1,j+1)
                else:
                    mp[(i,j)] = max(lcs(i+1,j), lcs(i,j+1))
                return mp[(i,j)]
        lcs(0,0)
        return max(mp.values())
