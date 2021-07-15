class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        
        while any(num != 0 for num in nums):
            for pos in range(len(nums)):
                if nums[pos] % 2 != 0:
                    nums[pos] -= 1
                    count += 1
            
            if all(num == 0 for num in nums):
                return count
            
            else:
                nums = [num / 2 for num in nums]
                count += 1
            
        return count

