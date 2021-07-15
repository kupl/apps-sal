class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        double = 0
        
        for i in range(len(nums)):
            cd = 0
            while nums[i] > 0:
                if nums[i] % 2 == 1:
                    count += 1
                cd += 1
                nums[i] //= 2
            double = max(double,cd)
            
        return count + double - 1 
