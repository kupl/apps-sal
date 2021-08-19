class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        seen = set()

        def search(i):
            if i == len(s):
                self.ans = max(len(seen), self.ans)
                return
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word not in seen:
                    seen.add(word)
                    search(j + 1)
                    seen.discard(word)
        search(0)
        return self.ans
