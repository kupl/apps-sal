class Solution:

    def __init__(self):
        self.ans = 0
        self.set = set()

    def maxUniqueSplit(self, s: str) -> int:
        self.solve(s, 0)
        return self.ans

    def solve(self, s: str, pos: int) -> None:
        if pos > len(s):
            return
        self.ans = max(self.ans, len(self.set))
        if self.ans - len(self.set) >= len(s) - pos:
            return
        for i in range(pos, len(s)):
            v = s[pos:i + 1]
            if v in self.set:
                continue
            self.set.add(v)
            self.solve(s, i + 1)
            self.set.remove(v)
