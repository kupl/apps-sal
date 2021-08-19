class Solution:

    def lenLongestFibSubseq(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for x in range(n)] for y in range(n)]
        max_ = 0
        for i in range(2, n):
            l = 0
            r = i - 1
            min_possible = nums[0] + nums[1]
            max_possible = nums[r] + nums[r - 1]
            if nums[i] < min_possible or nums[i] > max_possible:
                continue
            while l <= r:
                s = nums[l] + nums[r]
                if s > nums[i]:
                    r -= 1
                elif s < nums[i]:
                    l += 1
                else:
                    dp[r][i] = dp[l][r] + 1
                    max_ = max(max_, dp[r][i])
                    l += 1
                    r -= 1
        return max_ if max_ == 0 else max_ + 2
