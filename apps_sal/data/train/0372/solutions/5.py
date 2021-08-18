class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p and len(s) != 0:
            return False
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    res = i == len(s)
                else:
                    head_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        res = dp(i, j + 2) or head_match and dp(i + 1, j)
                    else:
                        res = head_match and dp(i + 1, j + 1)
                memo[(i, j)] = res
            return memo[(i, j)]

        return dp(0, 0)
