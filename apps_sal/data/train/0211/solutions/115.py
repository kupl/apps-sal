class Solution:
    def dfs(self, s, req_l, segs, cur, hs):
        if cur >= len(s):
            return segs == req_l

        for pos in range(cur, len(s)):
            ts = s[cur:pos + 1]
            if ts in hs:
                continue
            hs.add(ts)
            if self.dfs(s, req_l, segs + 1, pos + 1, hs):
                return True
            hs.remove(ts)
        return False

    def maxUniqueSplit(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            if self.dfs(s, i, 0, 0, set()):
                return i
        return 1
