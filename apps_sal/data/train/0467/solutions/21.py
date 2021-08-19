class Solution:

    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            divisor = 0
            a = 2
            upperLimit = int(num ** 0.5)
            if upperLimit ** 2 == num:
                continue
            upperLimit += 1
            subAns = 1 + num
            while a < upperLimit:
                if num % a == 0:
                    if divisor == 0:
                        divisor += 1
                        subAns += a + num // a
                    else:
                        break
                upperLimit = min(upperLimit, num // a)
                a += 1
            else:
                if divisor == 1:
                    ans += subAns
        return ans
