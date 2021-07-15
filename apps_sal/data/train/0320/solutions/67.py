class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        num = max(nums)
        res = 0

        for i in range(n):
            if nums[i] == 0:
                continue
                
            res += 1
            num = nums[i]
            while num > 1:
                res += num % 2
                num //= 2
    
        c = 0
        num = max(nums)
        while num > 1:
            num //= 2
            res += 1
        return res

