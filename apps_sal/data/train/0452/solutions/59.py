class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        def helper(i, d):
            if i == n and d == 0:
                return 0
            if d <= 0 or n - i < d:
                return float('inf')
            if (i, d) in memo:
                return memo[i, d]
            subGroupJobMax = -1
            memo[i, d] = float('inf')
            for j in range(i, n):
                subGroupJobMax = max(subGroupJobMax, jobDifficulty[j])
                result = subGroupJobMax + helper(j + 1, d - 1)
                memo[i, d] = min(memo[i, d], result)
            return memo[i, d]
        memo = {}
        ans = helper(0, d)
        return -1 if ans is None or ans == float('inf') else ans
