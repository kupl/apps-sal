class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        used = set()
        self.res = 1
        self.backtrack(s, 0, used)
        return self.res

    def backtrack(self, s, cur, used):
        if not s:
            self.res = max(self.res, cur)
            return
        for i in range(1, len(s) + 1):
            if s[:i] not in used:
                used.add(s[:i])
                self.backtrack(s[i:], cur + 1, used)
                used.remove(s[:i])
