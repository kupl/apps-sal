class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        ans = 0
        seen = {0: 0}
        for i in range(1, n + 1):
            curr = prefix[i]
            a = curr - target
            if a in seen:
                ans += 1
                seen = {}
            seen[curr] = i
        return ans
