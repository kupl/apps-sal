class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 1

        def rec(split, s):
            if not s:
                se = set(split)
                if len(se) == len(split):
                    self.ans = max(self.ans, len(split))
                return
            for i in range(len(s)):
                piece = s[0:i + 1]
                spl = split[:]
                spl.append(piece)
                rec(spl, s[i + 1:])
        rec([], s)
        return self.ans
