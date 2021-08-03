class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def helper(idx1, idx2):
            if len(text1) <= idx1 or len(text2) <= idx2:
                return 0
            if text1[idx1] == text2[idx2]:
                return 1 + helper(idx1 + 1, idx2 + 1)
            if text1[idx1] not in text2[idx2:]:
                return helper(idx1 + 1, idx2)
            else:
                newidx2 = idx2 + text2[idx2:].index(text1[idx1])
                return max(helper(idx1 + 1, newidx2 + 1) + 1, helper(idx1 + 1, idx2))
        return helper(0, 0)
