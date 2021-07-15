class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 0
        def dfs(node,seen):
            if node == len(s):
                self.ans = max(self.ans,len(seen))
            for i in range(node,len(s)):
                if s[node:i+1] not in seen:
                    dfs(i+1,seen|{s[node:i+1]})
        dfs(0,set())
        return self.ans
