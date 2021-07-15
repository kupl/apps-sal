class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        
        def lcs(left, right):
            nonlocal text1
            nonlocal text2
            if (left, right) in dp:
                return dp[(left, right)]
            if left >= len(text1) or right >= len(text2):
                return 0
            if text1[left] == text2[right]:
                count = 1 + lcs(left + 1, right + 1)
                dp[(left, right)] = count
                return count
            else:
                count = max(lcs(left + 1, right), lcs(left, right + 1))
                dp[(left, right)] = count
                return count
        return lcs(0, 0)
