class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = '@#' + '#'.join(s) + '#$'
        n = len(t)
        r = [0] * n
        c = 0
        for i in range(1, n - 1):
            if i - c < r[c]:
                if r[c - (i - c)] < r[c] - (i - c):
                    r[i] = r[c - (i - c)]
                else:
                    r[i] = r[c] - (i - c)
                    while t[i - r[i] - 1] == t[i + r[i] + 1]:
                        r[i] += 1
                    c = i
            else:
                r[i] = 0
                while t[i - r[i] - 1] == t[i + r[i] + 1]:
                    r[i] += 1
                c = i
        return sum((i + 1) // 2 for i in r)
