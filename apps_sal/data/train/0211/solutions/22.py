class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.seen = set()
        self.result = 0

        def backtrack(s, start):
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] not in self.seen:
                    self.seen.add(s[start:end])
                    if backtrack(s, end):
                        self.result = max(self.result, len(self.seen))
                    self.seen.remove(s[start:end])
            return False
        backtrack(s, 0)
        return self.result
