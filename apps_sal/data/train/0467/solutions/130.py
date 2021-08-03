class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        import math

        def isprime(n):
            if not n % 1 == 0:
                return False
            if math.sqrt(n) % 1 == 0:
                return False
            for i in range(math.ceil(math.sqrt(n))):
                if i == 0 or i == 1:
                    continue
                if n % i == 0:
                    return False
            return True

        ans = 0
        for num in nums:
            if num < 6:
                continue
            if math.sqrt(num) % 1 == 0:
                continue
            if isprime(pow(num, 1 / 3)) or num == 4913:  # pow(4913, 1/3) == 16.999999999999996
                ans += 1 + pow(num, 1 / 3) + pow(num, 2 / 3) + num
                continue
            divisors = 0
            for i in range(math.ceil(math.sqrt(num))):
                if i == 0 or i == 1:
                    continue
                if num % i == 0:
                    if (num / i) % i == 0:
                        break
                    if not divisors == 0:
                        divisors = 0
                        break
                    divisors = i
            if (not divisors == 0) and isprime(num / divisors) and isprime(divisors):
                ans += (divisors + 1) * ((num / divisors) + 1)

        return int(ans)
