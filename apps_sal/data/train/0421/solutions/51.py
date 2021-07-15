class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        ss = list(map(lambda x: ord(x) - ord('a'), s))
        xmax = max(ss)
        xs = [(x, i, i + 1) for i, x in enumerate(ss) if x == xmax]
        while len(xs) > 1:
            xt, xmax = [], -1
            for h, i, j in xs:
                if ((not xt) or xt[-1][2] <= i) and j < n:
                    if ss[j] > xmax:
                        xt = [(h * 26 + ss[j], i, j + 1)]
                        xmax = ss[j]
                    elif ss[j] == xmax:
                        xt.append((h * 26 + ss[j], i, j + 1))
                    xs = xt
        return s[xs[0][1]:]
