class Solution:

    def numWays(self, s: str) -> int:
        n = s.count('1')
        if n % 3 != 0:
            return 0
        if n == 0:
            return comb(len(s) - 1, 2) % (10 ** 9 + 7)
        (a, b, c, d) = self.findThirdOneInds(s, n)
        return (b - a) * (d - c) % (10 ** 9 + 7)

    def findThirdOneInds(self, s, n):
        out = []
        ind = -1
        for i in range(2 * n // 3 + 2):
            ind = s.find('1', ind + 1)
            if i == n // 3 - 1:
                out.append(ind)
            if i == n // 3:
                out.append(ind)
            if i == 2 * n // 3 - 1:
                out.append(ind)
            if i == 2 * n // 3:
                out.append(ind)
        return out
