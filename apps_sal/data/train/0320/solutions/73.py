class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while not all(ele < 2 for ele in nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    count += 1
                    
                nums[i] //= 2
            count += 1
            
        count += sum(ele == 1 for ele in nums)
        return count
