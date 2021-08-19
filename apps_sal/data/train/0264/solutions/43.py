class Solution:

    def maxLength(self, arr: List[str]) -> int:
        self.maxLen = 0

        def isUnique(s):
            return len(s) if len(s) == len(set(s)) else -1

        def dfs(i, s):
            if i == len(arr) and isUnique(s) > self.maxLen:
                self.maxLen = len(s)
                return
            if i == len(arr):
                return
            dfs(i + 1, s)
            dfs(i + 1, s + arr[i])
        dfs(0, '')
        return self.maxLen
