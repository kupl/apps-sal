class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def NOD(x):
            divisor = set()
            for i in range(1, int(sqrt(x)) + 1):
                if not x % i:
                    divisor.add(i)
                    divisor.add(x // i)
            return divisor

        res = 0
        for num in nums:
            divisor = NOD(num)
            if len(divisor) == 4:
                res += sum(divisor)
        return res
