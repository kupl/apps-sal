class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        def it():
            nonlocal ops
            postAllZero = True
            for i in range(len(nums)):
                n = nums[i]
                if n % 2 == 1:
                    nums[i] -= 1
                    ops += 1
                if nums[i] > 0:
                    postAllZero = False
            if postAllZero:
                return
            for i in range(len(nums)):
                nums[i] /= 2
            ops += 1
            it()
        it()
        return ops
