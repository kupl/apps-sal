class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        self.N = len(s)
        wordset = set(s)
        if len(wordset) >= self.N - 1:
            return len(wordset)
        self.cur = 0

        def dfs(i, visit, num):
            if self.N - i + num <= self.cur:
                return
            if s[i:] not in visit:
                self.cur = max(self.cur, num + 1)
            for j in range(i + 1, self.N):
                new = s[i:j]
                if new not in visit:
                    visit.add(new)
                    dfs(j, visit, num + 1)
                    visit.remove(new)
        visit = set()
        dfs(0, visit, 0)
        return self.cur
