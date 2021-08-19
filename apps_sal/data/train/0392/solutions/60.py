class Solution:

    def numWays(self, s: str) -> int:
        md = 10 ** 9 + 7
        res = 0
        n = len(s)
        n1 = sum(map(lambda x1: 1 if x1 == '1' else 0, s))
        if n > 2 and n1 % 3 == 0:
            x = n1 // 3
            x2 = x << 1
            if x == 0:
                res = (n - 1) * (n - 2) // 2
            else:
                (cnt, c1, c2) = (0, 0, 0)
                for (i, c) in enumerate(s):
                    if c == '1':
                        cnt += 1
                    if cnt == x:
                        c1 += 1
                    elif cnt == x2:
                        c2 += 1
                res = c1 * c2
        return res % md
