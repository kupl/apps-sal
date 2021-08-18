class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = {}

        def recursive_helper(left, right):
            if left > right:
                return 0

            pair = (left, right)
            if pair in dp:
                return dp[pair]
            dp[pair] = float('inf')
            for k in range(left + 1, right):
                dp[pair] = min(dp[pair], recursive_helper(left, k) + recursive_helper(k, right) + A[left] * A[k] * A[right])

            if dp[pair] == float('inf'):
                dp[pair] = 0

            return dp[pair]

        return recursive_helper(0, len(A) - 1)
