class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def deductOdd(nums):
            n = len(nums)
            cnt = 0
            for i in range(n):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    cnt += 1        
            return cnt
        
        def halfEven(nums):
            n = len(nums)
            allZero = True
            for i in range(n):
                if nums[i] > 0:
                    nums[i] //= 2
                    allZero = False
            return allZero
              
        result = deductOdd(nums)
        while not halfEven(nums):
            result += 1
            result += deductOdd(nums)
            
        return result
        

