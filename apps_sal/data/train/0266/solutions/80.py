class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) == 1:
            return 0

        lmap = collections.Counter(s[0:1])
        rmap = collections.Counter(s[1:])
        ans = 0
        for i in range(1, len(s)):
            if len(lmap) == len(rmap):
                ans += 1
            lmap.update([s[i]])
            rmap[s[i]] -= 1
            if not rmap[s[i]]:
                del rmap[s[i]]

        return ans
