class Solution:
        
    def minOperations(self, nums: List[int]) -> int:
        
        # we need to find out the maximum number of multiplications we need to do
        # how many mul will be required for largest number
        # all other muls can be arranged during the course
        # for ones, just need to make all odd numbers even
        # in every iteration
        twos = 0
        ones = 0
        for n in nums:
            mul = 0
            while n:
                if n%2:
                    n -=1
                    ones+=1
                else:
                    n = int(n/2)
                    mul +=1
            twos = max(twos,mul)
        
        return ones + twos
        
              
                    
        

