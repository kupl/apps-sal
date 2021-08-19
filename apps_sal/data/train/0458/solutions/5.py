class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # remove smallest thing from centert
        tot = sum(nums)
        need = sum(nums) % p
        if need == 0:
            return 0
        seen = {0: -1}
        curr = 0
        ret = len(nums)
        for i, num in enumerate(nums):
            curr = (curr + num) % p
            other = (curr - need) % p
            if other in seen:
                my_best = i - seen[other]
                if my_best < ret:
                    ret = my_best
            seen[curr] = i
        return ret if ret != len(nums) else -1
