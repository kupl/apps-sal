class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)

        @lru_cache(None)
        def dfs(index, remain, acc, size):
            if index >= N:
                return 0 if size == 0 else acc / size
            ans = 0
            if remain > 0:
                ans = max(ans, (acc + A[index]) / (size + 1) + dfs(index + 1, remain - 1, 0, 0))
            ans = max(ans, dfs(index + 1, remain, acc + A[index], size + 1))
            return ans

        return dfs(0, K - 1, 0, 0)
