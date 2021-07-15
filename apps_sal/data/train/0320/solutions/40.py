class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #m = max(nums)
        highest_bit = 0
        addone = 0
        for num in nums:
            tmp = -1
            while num > 0:
                addone += num & 1
                num >>= 1
                tmp += 1
            highest_bit = max(highest_bit, tmp)
        return highest_bit + addone

