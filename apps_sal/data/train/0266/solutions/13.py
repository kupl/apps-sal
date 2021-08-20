class Solution:

    def sub(self, h, h2):
        nh = h.copy()
        for k in h2:
            if k in nh:
                nh[k] = nh[k] - h2[k]
                if nh[k] == 0:
                    del nh[k]
        return nh

    def numSplits(self, s: str) -> int:
        h = {}
        for c in s:
            if c not in h:
                h[c] = 0
            h[c] = h[c] + 1
        ct = 0
        h2 = {}
        for (i, c) in enumerate(s):
            if c not in h2:
                h2[c] = 0
            h2[c] = h2[c] + 1
            uh = self.sub(h, h2)
            if len(h2) == len(uh):
                ct = ct + 1
        return ct
