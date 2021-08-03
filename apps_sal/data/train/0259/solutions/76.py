import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def get_sum(nmb):
            if nmb == 0:
                return False
            val = 0
            for num in nums:
                val += math.ceil(num / nmb)
            return val

        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if get_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid - 1

        if get_sum(left) <= threshold:
            return left
        return right


#     def get_sum(self, divisor, nums):
#         res = 0
#         for n in nums:
#             tmp = n // divisor
#             if tmp * divisor < n:
#                 tmp += 1

#             res += tmp

#         return res

#         def chk(nmb):
#             if nmb == 0:
#                 return False
#             val = 0
#             for num in nums:
#                 val += math.ceil(num/nmb)
#                 if val > threshold:
#                     return False
#             return True

#         high = max(nums)
#         low = high//threshold
#         while low <= high:
#             mid = (low + high)//2

#             if chk(mid):
#                 high = mid - 1
#             elif not chk(mid):
#                 low = mid + 1
#         return low-1 if chk(low-1) else high+1
