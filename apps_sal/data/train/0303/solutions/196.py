class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        def dfs(start, memo):
            if start in memo:
                return memo[start]
            N = len(A)
            if start >= N:
                return 0
            maxSum = 0
            maxEle = 0
            for i in range(start, min(N, start + K)):
                maxEle = max(maxEle, A[i])
                maxSum = max(maxSum, maxEle * (i - start + 1) + dfs(i + 1, memo))
            memo[start] = maxSum
            return maxSum
        return dfs(0, {})
