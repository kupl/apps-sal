class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:

        def four_div_sum(num):
            divs = set()
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    divs.update({i, num // i})
                if len(divs) > 4:
                    return 0
            return sum(divs) if len(divs) == 4 else 0
        return sum((four_div_sum(num) for num in nums))
