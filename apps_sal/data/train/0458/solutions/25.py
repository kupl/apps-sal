class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mod = sum(nums) % p
        if mod == 0:
            return 0
        ans = float('inf')
        pos = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total = (total + num) % p
            target = (total - mod) % p
            if target in pos:
                ans = min(ans, i - pos[target])
            pos[total] = i

        return ans if ans < len(nums) else -1
