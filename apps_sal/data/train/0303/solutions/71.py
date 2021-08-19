class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.dp = [-1] * (len(arr) + k)
        return self.solve(arr, 0, k)

    def solve(self, arr, start, k):
        if start >= len(arr):
            return 0
        if start + k >= len(arr):
            end = min(len(arr), start + k)
            return max(arr[start:end]) * (end - start)
        if self.dp[start] != -1:
            return self.dp[start]
        result = float('-inf')
        for p in range(1, k + 1):
            temp = max(arr[start:start + p]) * p + self.solve(arr, start + p, k)
            result = max(temp, result)
        self.dp[start] = result
        return result
