class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        lc = [1]*n
        rc = [1]*n
        ls = set()
        rs = set()
        for i in range(n):
            ls.add(s[i])
            rs.add(s[-(i+1)])
            lc[i] = len(ls)
            rc[-(i+1)] = len(rs)
        r = 0
        for i in range(n-1):
            if lc[i]==rc[i+1]: r+=1
        return r
