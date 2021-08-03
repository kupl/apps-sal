class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(i):
            if i >= len(s):
                return len([v for v in t.values() if v])
            best = 0
            for j in range(i, len(s)):
                ss = s[i:j + 1]
                t[ss] += 1
                best = max(best, split(j + 1))
                t[ss] -= 1
            return best

        t = collections.defaultdict(int)
        return split(0)
