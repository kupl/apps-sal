class Solution:

    def __init__(self):
        self.divisors = {}

    def count_divisors(self, n):
        if n in self.divisors:
            return self.divisors[n]
        result = []
        counter = 1
        quo = n // counter
        while counter <= quo:
            if n % counter == 0:
                result.append(counter)
                if quo != counter:
                    result.append(quo)
            counter += 1
            quo = n // counter
        self.divisors[n] = result
        return result

    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors = list(map(self.count_divisors, nums))
        four_divisors = list([x for x in divisors if len(x) == 4])
        return sum(map(sum, four_divisors))
