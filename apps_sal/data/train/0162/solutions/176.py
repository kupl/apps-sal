class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        l1 = len(text1)
        l2 = len(text2)
        if l1 == 0 or l2 == 0:
            return 0
        for i, c1 in enumerate(text1):
            common = False
            for j, c2 in enumerate(text2):
                seq = 0
                if c1 == c2:
                    if (i - 1, j - 1) in dp:
                        seq = max(seq, dp[(i - 1, j - 1)])
                    seq += 1
                else:
                    if (i, j - 1) in dp:
                        seq = max(seq, dp[(i, j - 1)])
                    if (i - 1, j) in dp:
                        seq = max(seq, dp[(i - 1, j)])
                dp[(i, j)] = seq
        return dp[(l1 - 1, l2 - 1)]
