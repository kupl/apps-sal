class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = -1
        for bit in range(1 << n - 1):
            sep = []
            for i in range(n - 1):
                if bit >> i & 1:
                    sep.append(i + 1)
            sep.append(n)
            ww = set()
            l = r = 0
            ng = False
            for r in sep:
                w = s[l:r]
                if w in ww:
                    ng = True
                    break
                ww.add(w)
                l = r
            if ng:
                continue
            ans = max(ans, len(ww))
        return ans
