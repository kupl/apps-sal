class Solution:
    def maxUniqueSplit(self, string: str) -> int:

        def split(s, splits):
            maxs = 1 if s not in splits else 0
            for i in range(1, len(s)):
                if s[:i] in splits:
                    continue
                rst = 1 + split(s[i:], splits + [s[:i]])
                maxs = max(rst, maxs)
            return maxs

        return split(string, [])
