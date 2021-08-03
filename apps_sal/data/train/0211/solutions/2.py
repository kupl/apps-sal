class Solution:
    def maxUniqueSplit(self, s: str, mem=None, seen=None) -> int:
        if mem is None:
            mem = {}
        if seen is None:
            seen = set()

        res = 0
        for i in range(0, len(s)):
            if s[0:i + 1] in seen:
                continue
            seen.add(s[0:i + 1])
            res = max(res, 1 + self.maxUniqueSplit(s[i + 1:], mem, seen))
            seen.remove(s[0:i + 1])
        mem[s] = res

        return res
