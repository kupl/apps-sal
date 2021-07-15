class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            if nums[0] == 1:
                return True
            else:
                return False
            
        now = -1
        for i in range(1, len(nums)):
            if i == 1:
                now = math.gcd(nums[i-1], nums[i])
            else:
                now = math.gcd(nums[i],now)
            
        
        if now == 1:
            return True
        return False
