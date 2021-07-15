class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if r == 0:
            return 0
        res, prefix, cur = len(nums), {0: -1}, 0
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            prefix[cur] = i
            target = (cur - r) % p
            if target in prefix and res > i - prefix[target]:
                res = i - prefix[target]
        return res if res < len(nums) else -1
