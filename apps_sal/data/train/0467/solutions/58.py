class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        summ = 0
        for num in nums:
            if num > 1:
                summ += self.divisors(num)
        
        return summ
    
    def divisors(self, num):
        visited_factors = set()
        visited_factors.add(1)
        visited_factors.add(num)
        factors = 2
        summ = 1 + num
        for i in range(2, int(num ** 0.5) + 1):
            # print(\"i \", i, \" num \", num)
            if not num % i and num % i not in visited_factors:
                visited_factors.add(i)
                summ += i
                factors += 1
                secondHalf = num // i
                if secondHalf not in visited_factors:
                    visited_factors.add(secondHalf)
                    factors += 1
                    summ += secondHalf
        
        # print(\"factors \", factors)
        if factors == 4:
            return summ
        return 0
