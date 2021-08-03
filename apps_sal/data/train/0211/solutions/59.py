class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        self.res = 1

        def backtrack(curr, idx):
            if len(curr) != len(set(curr)):
                return
            else:
                if idx == len(s):
                    self.res = max(self.res, len(curr))
                    return
            for i in range(idx + 1, len(s) + 1):
                backtrack(curr + [s[idx: i]], i)

        backtrack([], 0)

        return self.res
