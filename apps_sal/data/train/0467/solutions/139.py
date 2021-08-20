class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisor_num = set()
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    divisor_num.add(num // i)
                    divisor_num.add(i)
            if len(divisor_num) == 4:
                res += sum(divisor_num)
        return res
