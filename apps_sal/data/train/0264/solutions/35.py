# https://www.youtube.com/watch?v=N7womGmLXh8
# https://www.youtube.com/watch?v=pD3cHFNyW2I
class Solution:
    # backtracking
    def maxLength(self, arr: List[str]) -> int:
        self.maxLen = 0
        def isUnique(s):
            return len(s) if len(s) == len(set(s)) else -1
        def dfs(i, s):
            if i == len(candi) and isUnique(s) > self.maxLen:
                self.maxLen = len(s)
                return
            if i == len(candi):
                return
            dfs(i + 1, s)  # use arr[i]
            dfs(i + 1, s + candi[i])  # without using arr[i]
            
        candi = []
        for ss in arr:
            if isUnique(ss) > 0:
                candi.append(ss)
    
        dfs(0, '')
        return self.maxLen

