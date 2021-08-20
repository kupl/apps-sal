class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret += self.has_four_divisors(num)
        return int(ret)

    def has_four_divisors(self, num):
        divisor_sum = 0
        divisors = 0
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                if i != num / i:
                    divisors += 2
                    divisor_sum += i
                    divisor_sum += num / i
                else:
                    divisors += 1
                    divisor_sum += i
        if divisors == 4:
            return divisor_sum
        return 0
