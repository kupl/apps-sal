class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        
        def check_all_zeros(arr):
            for ele in arr:
                if ele != 0:
                    return False
            return True 
        
        def divide_by_2(arr):
            return list([x/2 for x in arr])
        
        ops = 0
        
        while True:
            
            if check_all_zeros(nums):
                return ops
        
            all_even = True
            for i in range(length):
                num = nums[i]
                if num % 2 == 0:
                    if i == length - 1 and all_even:
                        nums = divide_by_2(nums)
                        ops += 1

                else:
                    all_even = False
                    nums[i] -= 1
                    ops += 1     
                

