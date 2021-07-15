class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ans = len(nums)
        diff = sum(nums) % p
        total = 0
        cmods = {}
        for i, x in enumerate(nums):
            total += x
            target = (total - diff) % p
            if total % p == diff:
                ans = min(ans, i+1)
            if target in cmods:
                ans = min(ans, i-cmods[target])
            cmods[total % p] = i
        if total % p == 0:
            return 0
        return ans if ans != len(nums) else -1
