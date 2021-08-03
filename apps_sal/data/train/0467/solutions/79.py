class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            divisor = set()
            for i in range(1, floor(sqrt(n)) + 1):
                if n % i == 0:
                    divisor.add(n // i)
                    divisor.add(i)
                    if len(divisor) > 4:
                        break
            if len(divisor) == 4:
                res += sum(divisor)

        return res
