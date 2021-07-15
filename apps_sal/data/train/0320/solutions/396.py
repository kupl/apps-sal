class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ret = 0
        def check(nums):
            isAllZero = 1
            multiplied = 0
            res = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    isAllZero = 0
                if nums[i] & 1:
                    res += 1
                    nums[i] -= 1
                if nums[i] != 0:
                    nums[i] = nums[i] // 2
                    multiplied = 1
            if multiplied == 1:
                res += 1
            return (isAllZero, res)
        
        while True:
            done, cnt = check(nums)
            ret += cnt
            if done == 1:
                break
        return ret
        
        

                    

