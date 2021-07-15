class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        end = len(nums)-1
        nums.sort()
        for i in range(len(nums)):
            while nums[i] + nums[end] > target:
                if end > i:
                    end = end-1
                else:
                    return res % (10**(9)+7)
            res += pow(2, end - i)
        return res % (10**(9)+7)
