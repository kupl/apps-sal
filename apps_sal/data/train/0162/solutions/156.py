def dp(s1, s2, i, j, mem):
    if i >= len(s1) or j >= len(s2):
        return 0
    elif (i, j) in mem:
        return mem[(i, j)]

    l = dp(s1, s2, i + 1, j, mem)
    r = dp(s1, s2, i, j + 1, mem)
    both = (1 + dp(s1, s2, i + 1, j + 1, mem)) if s1[i] == s2[j] else 0
    res = max(r, l, both)
    mem[(i, j)] = res
    return res


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return dp(text1, text2, 0, 0, {})
