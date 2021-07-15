class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:    
        factors_cache = {}
        
        def get_factors(num):
            if num in factors_cache:
                return factors_cache[num]
            else:
                factors = set([1, num])
                for potential_divisor in range(2, math.ceil(math.sqrt(num))):
                    if num % potential_divisor == 0:
                        factors = factors.union(get_factors(potential_divisor))
                        factors = factors.union(get_factors(num // potential_divisor))
                    if len(factors) > 4:
                        break
                factors_cache[num] = factors
                return factors
            
        running_sum = 0
        for num in nums:
            factors = get_factors(num)
            if len(factors) == 4:
                running_sum += sum(factors)
            
        return running_sum

