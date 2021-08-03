# class Solution:
#     def smallestDivisor(self, nums: List[int], threshold: int) -> int:

#         def check(divisor):
#             res = 0
#             for num in nums:
#                 if num % divisor == 0:
#                     res += num // divisor
#                 else:
#                     res += (num // divisor) + 1
#             if res <= threshold:
#                 return True
#             return False

#         left = 1
#         right = 1000000 #最大元素700ms
#         # right = 1 800ms
#         # for num in nums:
#         #     right = max(right, num)
#         while left < right:
#             mid = (left + right) >> 1
#             if check(mid) == True:
#                 right = mid
#             else:
#                 left = mid+1

#         return left

from numpy import array, ceil, sum


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums = array(nums)
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if sum(ceil(nums / mid)) <= threshold:
                r = mid
            else:
                l = mid + 1
        return r
