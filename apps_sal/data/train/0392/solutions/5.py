class Solution:
    def numWays(self, s: str) -> int:
        res = 0
        c = collections.Counter(s)
        print(c)
        tot = c['1']
        if tot % 3:
            return 0
        mod = 10**9 + 7
        if tot == 0:
            n = len(s) - 1
            return ((n * (n - 1)) // 2) % mod

        ctr = 0
        res = 1

        eq = tot // 3
        a, b, c, d = -1, -1, -1, -1
        for i, ch in enumerate(s):

            if ch == '1':
                ctr += 1

            if a < 0 and ctr == eq:
                a = i
            if b < 0 and ctr == eq + 1:
                b = i
            if c < 0 and ctr == 2 * eq:
                c = i
            if d < 0 and ctr == 2 * eq + 1:
                d = i

        return (((b - a) % mod) * ((d - c) % mod)) % mod
