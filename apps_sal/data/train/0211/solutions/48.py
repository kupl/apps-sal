class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        self.s = s
        self.cache = {}
        count = self.maxUniqueSplitHelper(0, set())
        return count

    def maxUniqueSplitHelper(self, pos: int, substrings: set) -> int:
        hashed = frozenset(substrings)
        if (pos, hashed) in self.cache:
            return self.cache[pos, hashed]
        if pos == len(self.s):
            return len(substrings)
        count = 0
        for i in range(pos, len(self.s)):
            substring = self.s[pos:i + 1]
            if substring in substrings:
                continue
            substrings.add(substring)
            count = max(count, self.maxUniqueSplitHelper(i + 1, substrings))
            substrings.remove(substring)
        self.cache[pos, hashed] = count
        return count
