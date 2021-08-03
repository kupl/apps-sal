from math import sqrt


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            divisor = set()
            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    divisor.add(num // i)
                    divisor.add(i)
                if len(divisor) > 4:
                    break

            if len(divisor) == 4:
                res += sum(divisor)
        return res

# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int: #o(n^2)
#         ans = 0
#         for num in nums:
#             if Solution.findNumDivisors(self,num) == 4:
#                 ans += Solution.sumDivisors(self,num)

#         return ans

#     def findNumDivisors(self, num) -> int: #o(N)
#         cnt = 1

#         for i in range(1,int(sqrt(num))):
#             if num % i == 0:
#                 cnt += 1

#         return cnt

#     def sumDivisors(self, num) -> int:
#         ans = num

#         for i in range(1,int(sqrt(num)):
#             if num % i == 0:
#                 ans += i

#         return ans
