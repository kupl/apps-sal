class Solution:

    def minOperations(self, nums: List[int]) -> int:
        (res, val) = (0, sum(nums))
        while val:
            val0 = val
            for (i, x) in enumerate(nums):
                if x % 2:
                    nums[i] -= 1
                    val -= 1
            res += val0 - val
            if val == val0:
                for i in range(len(nums)):
                    nums[i] //= 2
                val //= 2
                res += 1
        return res
