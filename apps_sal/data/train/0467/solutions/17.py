class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def count_divisors(x):
            num_divisors = 0
            sum_divisors = 0
            if sqrt(x) == int(sqrt(x)):
                num_divisors += 1
                sum_divisors += sqrt(x)
            for i in range(1, ceil(sqrt(x))):
                if x % i == 0:
                    num_divisors += 2
                    sum_divisors += i + (x // i)
            return sum_divisors if num_divisors == 4 else 0
        return sum([count_divisors(x) for x in nums])
