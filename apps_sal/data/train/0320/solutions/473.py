class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        changed = True
        while changed:

            changed = False
            for i, x in enumerate(nums):
                if not x % 2 == 0:
                    nums[i] -= 1
                    ops += 1
                    changed = True
            divided = False

            for i, x in enumerate(nums):
                if x > 0:
                    nums[i] = nums[i] // 2
                    divided = True

            if divided:
                changed = True
                ops += 1
        return ops
