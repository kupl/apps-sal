class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        res = 0
        n = len(arr)
        self.m = [0] * n
        for i in range(n):
            ans = self.dfs(arr, d, i)
            res = max(ans, res)
        return res

    def dfs(self, arr, d, i):
        res = 1
        if self.m[i] != 0:
            return self.m[i]
        for k in range(1, d + 1):
            if i + k >= len(arr):
                break
            if arr[i + k] >= arr[i]:
                break
            ans = self.dfs(arr, d, i + k) + 1
            if ans > res:
                res = ans
        for k in range(1, d + 1):
            if i - k < 0:
                break
            if arr[i - k] >= arr[i]:
                break
            ans = self.dfs(arr, d, i - k) + 1
            if ans > res:
                res = ans
        self.m[i] = res
        return res
