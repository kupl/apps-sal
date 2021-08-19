from functools import lru_cache


class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        c = []
        idx = 0
        tmp = 0
        while idx < len(s):
            if idx >= 1 and s[idx] != s[idx - 1]:
                c.append((s[idx - 1], tmp))
                tmp = 1
            else:
                tmp += 1
            if idx == len(s) - 1 and (len(c) == 0 or c[-1][0] != s[idx]):
                c.append((s[idx], tmp))
            idx += 1

        def rl(x):
            if x[1] == 1:
                return 1
            if 2 <= x[1] < 10:
                return 2
            if x[1] == 100:
                return 4
            return 3
        if len(s) >= 100 and len(c) == 1:
            return rl(c[0])

        @lru_cache(None)
        def dfs(i, r, prev=None, d=False):
            if i == len(c):
                return 0
            out = dfs(i + 1, r, c[i]) + rl(c[i])
            if r >= c[i][1] and (not d):
                if i + 1 < len(c) and prev and (prev[0] == c[i + 1][0]):
                    c[i + 1] = (c[i + 1][0], c[i + 1][1] + prev[1])
                    out = min(out, dfs(i + 1, r - c[i][1], prev, True) - rl(prev))
                    c[i + 1] = (c[i + 1][0], c[i + 1][1] - prev[1])
                else:
                    out = min(out, dfs(i + 1, r - c[i][1], prev))
            if c[i][1] >= 10 and r - c[i][1] + 9 >= 0:
                out = min(out, dfs(i + 1, r - c[i][1] + 9, (c[i][0], 9)) + 2)
            if c[i][1] >= 2 and r - c[i][1] + 1 >= 0:
                out = min(out, dfs(i + 1, r - c[i][1] + 1, (c[i][0], 1)) + 1)
            return out
        return dfs(0, k)
