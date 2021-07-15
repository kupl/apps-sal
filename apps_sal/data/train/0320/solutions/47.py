class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def ops(num):
            plus = 0
            mult = 0
            while num:
                if num % 2:
                    plus += 1
                    num -= 1
                else:
                    num //= 2
                    mult +=1
            return plus, mult
    
        plus = 0
        mult = 0
        for num in nums:
            plus_, mult_ = ops(num)
            plus += plus_
            mult = max(mult, mult_)
        return plus + mult
                
           
            

