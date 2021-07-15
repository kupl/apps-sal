class Solution:
    def lastSubstring(self, s: str) -> str:
        aMax = max(a for a in s)
        inds = [i for i in range(len(s)) if s[i] == aMax]
        sMax = ''
        for i in inds:
            sMax = max(sMax,s[i:])
            # print(sMax, inds)
        return sMax

