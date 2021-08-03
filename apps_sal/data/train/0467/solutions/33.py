class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            divs = self.divisors(num)
            if len(divs) == 4:
                ret += sum(divs)

        return ret

    def divisors(self, num):
        ret = []
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                ret += [i]
                if num // i != i:
                    ret += [num // i]

        return ret
