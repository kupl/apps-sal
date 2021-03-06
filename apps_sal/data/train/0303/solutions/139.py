class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k == n:
            return n * max(arr)
        dp = collections.deque([0] * k)
        for i in range(n - 1, -1, -1):
            m = 0
            result = 0
            for j in range(min(k, n - i)):
                m = max(m, arr[i + j])
                result = max(result, m * (j + 1) + dp[j])
            dp.appendleft(result)
            dp.pop()
        return dp[0]
