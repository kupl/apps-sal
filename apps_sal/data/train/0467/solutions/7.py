class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # find all divisor of this number and use set() to select all the distinct factors
        res = 0
        for num in nums:
            divisor_num = set()
            for i in range(1, int(sqrt(num))+1):
                if num%i == 0:
                    divisor_num.add(num//i)
                    divisor_num.add(i)
                    
            if len(divisor_num) == 4:
                res +=sum(divisor_num)
                
                
                
        #capital one len(divisor_num)==3, divisor_sum.remove(num)
                
                
                
        return res
                
                    
                    

