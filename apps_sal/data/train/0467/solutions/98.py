class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def divisors(v):
            divs = set()
            for i in range(1, ceil(sqrt(v)) + 1):
                if not v % i:
                    divs.update({i, v // i})
                if len(divs) > 4:
                    return 0
            return sum(divs) if len(divs) == 4 else 0

        return sum(map(divisors, nums))
