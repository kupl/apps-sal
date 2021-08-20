class Solution:
    book = set()

    def maxUniqueSplit(self, s):
        result = 0
        for i in range(1, len(s) + 1):
            curr = s[:i]
            if curr not in self.book:
                self.book.add(curr)
                result = max(result, 1 + self.maxUniqueSplit(s[i:]))
                self.book.remove(curr)
        return result
