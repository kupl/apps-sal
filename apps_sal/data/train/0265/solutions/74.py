class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        seen = {0: 0}
        ans = 0
        for i in range(1, n + 1):
            cur = prefix[i]
            a = cur - target
            if a in seen:
                ans += 1
                seen = {}
            seen[cur] = 1
        return ans
