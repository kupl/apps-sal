from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        n = len(nums)
        max_val = 0
        for i in range(n-1):
            for j in range(i+1, n):
                diff = nums[i] - nums[j]
                dp[(j, diff)] = 1 + dp[(i, diff)]
                max_val = max(max_val, dp[(j,diff)])
        return max_val + 1
