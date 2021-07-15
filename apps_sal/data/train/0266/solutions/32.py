class Solution:
    def numSplits(self, s: str) -> int:
        lc, rc = [], []
        ls, rs = set(), set()
        for c in s:
            ls.add(c)
            lc.append(len(ls))
        for c in reversed(s):
            rs.add(c)
            rc.append(len(rs))
        res = 0
        rc = rc[::-1]
        for i in range(len(lc) -  1):
            if lc[i] == rc[i + 1]:
                res += 1
        return res
