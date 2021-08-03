class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def explore(seen, s):
            for i in range(1, len(s)):
                word, other = s[:i], s[i:]
                if word in seen:
                    continue
                explore(seen + [word], other)
            else:
                if s in seen:
                    self.res = max(len(seen), self.res)
                else:
                    self.res = max(len(seen) + 1, self.res)

        self.res = 0
        explore([], s)
        return self.res
