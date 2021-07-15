class Solution:
    def __init__(self):
        self.result = 0

    def maxUniqueSplit(self, s: str) -> int:
        if not s:
          return 0
        def backtrack(start, cur):
            if start == len(s):
                self.result = max(self.result, len(set(cur)))
                return

            for i in range(start, len(s)):
                cur += [s[start:i+1]]
                backtrack(i + 1, cur)
                cur.pop()

        backtrack(0, [])

        return self.result
