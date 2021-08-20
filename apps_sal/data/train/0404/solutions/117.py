class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)

        @lru_cache(None)
        def dfs(index, remain):
            if remain <= 0:
                return sum(A[index:]) / (N - index)
            if index >= N:
                return 0
            ans = 0
            for i in range(index + 1, N):
                ans = max(ans, sum(A[index:i]) / (i - index) + dfs(i, remain - 1))
            return ans
        res = dfs(0, K - 1)
        return res
