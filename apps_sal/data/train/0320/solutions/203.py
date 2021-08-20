class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def L(x):
            return len(x)
        op = 0
        while sum(nums):
            isodd = False
            for i in range(L(nums)):
                if nums[i] & 1:
                    nums[i] -= 1
                    isodd = True
                    op += 1
            if not isodd:
                for i in range(L(nums)):
                    nums[i] >>= 1
                op += 1
        return op
