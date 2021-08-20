class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        self.answer = 0
        substrings = []

        def backtrack(start_i):
            if start_i == len(s):
                self.answer = max(self.answer, len(set(substrings)))
                return
            for j in range(start_i + 1, len(s) + 1):
                substrings.append(s[start_i:j])
                backtrack(j)
                substrings.pop()
        backtrack(0)
        return self.answer
