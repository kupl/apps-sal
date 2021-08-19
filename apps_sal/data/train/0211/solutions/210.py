class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        self.max = 0
        self.backtrack(s, set(), 0)
        return self.max

    def backtrack(self, s, store, l):
        if l >= len(s):
            self.max = max(self.max, len(store))
        for i in range(l, len(s) + 1):
            if s[l:i] not in store and l != i:
                store.add(s[l:i])
                self.backtrack(s, store, i)
                store.remove(s[l:i])
