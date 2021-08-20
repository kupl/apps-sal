class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        if need == 0:
            return 0
        pos = {0: -1}
        total = 0
        ans = float('inf')
        for (i, num) in enumerate(nums):
            total = (total + num) % p
            target = (total - need) % p
            if target in pos:
                ans = min(ans, i - pos[target])
            pos[total] = i
        return ans if ans < len(nums) else -1
