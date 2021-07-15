import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            divisors = self.getDivisors(num)
            if len(divisors) == 4:
                print(divisors, num)
                total+=sum(divisors)
        return total
    
    def getDivisors(self, num):
        res = set([1, num])
        for i in range(2,1+math.ceil(math.sqrt(num))):
            if num%i == 0:
                res.add(i)
                res.add(num//i)
        return res 
