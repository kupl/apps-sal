class Solution:
    def numWays(self, s: str) -> int:
        ttt = 10**9 + 7
        zs = list(map(len, s.split('1')))

        if not (len(zs) - 1) % 3 == 0:
            return 0
        if len(zs) == 1:
            return (len(s) - 1) * (len(s) - 2) // 2 % ttt
        ps = len(zs) // 3
        return (zs[ps] + 1) * (zs[ps * 2] + 1) % ttt
