class Solution:

    def longestPrefix(self, st: str) -> str:
        a = st
        l = len(a)
        i = 1
        leng = 0
        lps = [0]
        while i < l:
            if a[i] == a[leng]:
                leng += 1
                lps.append(leng)
                i += 1
            elif leng > 0:
                leng = lps[leng - 1]
            else:
                lps.append(0)
                i += 1
        return st[:lps[-1]]
