class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(s, n):
            if n < 0:
                return [[s]]
            else:
                res = []
                for i in range(1, len(s) - n):
                    for group in dfs(s[i:], n - 1):
                        res.append([s[:i]] + group)
                return res
            
        res = 1
        for i in range(len(s)):
            for group in dfs(s, i):
                res = max(res, len(set(group)))         
        return res
