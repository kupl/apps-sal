class Solution:
    def uniquelen(self, cur):
        if len(cur) == len(set(cur)):
            return(len(cur))
        else:
            return(-1)

    def dfs(self, arr, index, cur):
        if index == len(arr) and self.uniquelen(cur) > self.ans:
            self.ans = self.uniquelen(cur)
            return
        if index == len(arr):
            return

        self.dfs(arr, index + 1, cur)
        self.dfs(arr, index + 1, cur + arr[index])

    def maxLength(self, arr: List[str]) -> int:
        self.ans = -1
        self.dfs(arr, 0, '')
        return(self.ans)
