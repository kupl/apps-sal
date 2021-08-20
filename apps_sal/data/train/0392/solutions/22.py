class Solution:

    def numWays(self, s: str) -> int:
        all = s.count('1')
        if all == 0:
            if len(s) % 2 == 0:
                (c1, c2) = (int((len(s) - 2) / 2), len(s) - 1)
            else:
                (c1, c2) = (int((len(s) - 1) / 2), len(s) - 2)
            return self.modres(c1, c2)
        if all % 3 != 0:
            return 0
        one = all / 3
        c1 = self.check(s, one)
        c2 = self.check(s[::-1], one)
        return self.modres(c1, c2)

    def modres(self, c1, c2):
        mod = pow(10, 9) + 7
        return c1 % mod * c2 % mod % mod

    def check(self, s, one):
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
                if count == one:
                    p1 = i
                elif count > one:
                    p2 = i
                    break
        return p2 - p1
