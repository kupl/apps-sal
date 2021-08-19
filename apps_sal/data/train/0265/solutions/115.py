"""
sliding window approach

initalize left at 0, curr at 0
enumerate through right


"""


class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        seen = {0: 0}
        ans = 0
        for i in range(1, n + 1):
            curr = presum[i]
            prev = curr - target
            if prev in seen:
                ans += 1
                seen = {}
            seen[curr] = i
        return ans
