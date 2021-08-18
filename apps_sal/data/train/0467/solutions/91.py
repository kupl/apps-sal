from math import sqrt


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        sum_of_factor = 0

        for x in nums:

            factors = set()

            for i in range(1, int(sqrt(x) + 1)):

                if x % i == 0:

                    factors.add(i)
                    factors.add(x // i)

                    if len(factors) > 4:
                        break

            if len(factors) == 4:
                sum_of_factor += sum(factors)

        return sum_of_factor
