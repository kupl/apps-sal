class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = {}

        def dp(i, j):
            print((i, j))
            if (i, j) not in m:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                m[i, j] = ans
            return m[i, j]

        return dp(0, 0)
