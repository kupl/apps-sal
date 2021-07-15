class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while sum(nums) > 0:
            can_divide = False
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    ans += 1
                    nums[i] -= 1
                if nums[i] > 0:
                    can_divide = True
                    
            if can_divide:
                ans += 1
                for i in range(len(nums)):
                    nums[i] //= 2
                
        return ans

