class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ls = len(s)
        sl = ls - 1
        ps = 1 << (sl)
        ans = 0
        for i in range(ps):
            bi = bin(i)[2:].zfill(sl)  # 0 is a stick
            si = [0] + [j + 1 for j in range(sl) if bi[j] == '0'] + [sl + 1]
            lsi = len(si)
            ds = set([s[si[j]:si[j + 1]] for j in range(lsi - 1)])
            if len(ds) == lsi - 1:
                ans = max(ans, lsi - 1)
        return ans
