class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        n = len(s)
        def backtrack(start, have):
            if start>=n:
                self.ans=max(self.ans, len(have))
                return
            for i in range(start+1, n+1):
                tmp = s[start:i]
                if tmp in have: continue
                else:
                    have.add(tmp)
                    backtrack(i, have)
                    have.remove(tmp)
        backtrack(0, set())
        return self.ans

