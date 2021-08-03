class Solution:
    def minOperations(self, nums, op=0):
        isum = 0
        e = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                op = op + 1
                nums[i] = (nums[i] - 1)
                if nums[i] != 0:
                    e = 1
                    nums[i] = nums[i] / 2
            else:
                if nums[i] != 0:
                    e = 1
                    nums[i] = nums[i] / 2
            isum = isum + nums[i]
        op = op + e
        if isum == 0:
            return op
        return self.minOperations(nums, op)
