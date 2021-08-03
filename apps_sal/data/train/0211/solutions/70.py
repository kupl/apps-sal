class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def solve(last, idx, cur):
            if idx == len(s):
                if len(cur) == len(set(cur)):
                    self.ans = max(self.ans, len(cur))
                return

            cur.append(s[last:idx + 1])
            solve(idx + 1, idx + 1, cur)
            cur.pop()

            solve(last, idx + 1, cur)
        self.ans = 0
        solve(0, 0, [])
        return self.ans
