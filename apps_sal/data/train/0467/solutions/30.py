class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            divisors = set()
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
            if len(divisors) == 4:
                ans += sum(divisors)

        return ans
