class Solution:
    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        n = len(nums)
        idx = {n: i for i, n in enumerate(nums)}
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = 2
            dp[j][j] = 1
        ans = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                if nums[i] <= nums[j] // 2:
                    dp[i][j] = 2
                else:
                    prev = nums[j] - nums[i]
                    if prev in idx:
                        dp[i][j] = dp[idx[prev]][i] + 1
                    else:
                        dp[i][j] = 2
                ans = max(ans, dp[i][j])
        return ans if ans > 2 else 0
