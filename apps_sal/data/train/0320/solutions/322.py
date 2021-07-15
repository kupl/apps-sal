class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        mmax = float('inf')
        while mmax > 0:
            mmax = 0
            for i in range(len(nums)):
                if nums[i]&1 == 1:
                    nums[i] -= 1
                    res += 1
                mmax = max(mmax, nums[i])
            if mmax > 0:
                nums = [x//2 for x in nums]
                res += 1
        return res
                    

