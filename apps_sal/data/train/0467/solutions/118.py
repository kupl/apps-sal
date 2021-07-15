class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for n in nums:
            divisors = set()
            for i in range(1,math.floor(n**(0.5)) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n/i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                ret += sum(divisors) 
            
        return int(ret)

