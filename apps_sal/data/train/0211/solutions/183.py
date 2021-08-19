class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        self.S = 0

        def dfs(s, tmp):
            if s == '':
                self.S = max(self.S, len(tmp))
            for i in range(1, len(s) + 1):
                if s[:i] not in tmp:
                    dfs(s[i:], tmp + [s[:i]])
        dfs(s, [])
        return self.S
