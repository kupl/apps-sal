import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def ok(mid):
            ans = 0
            for num in nums:
                ans += math.ceil(num / mid)
                if ans > threshold:
                    return False
            return True
        l, r = 1, int(1e6)
        while l <= r:
            mid = (l + r) // 2
            if ok(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
#         nums.sort()

#         v1 = sum(nums)
#         v2 = len(nums)
#         if v1<= threshold:
#             return 1
#         l = 1
#         u = max(nums)

#         addl = []
#         while l+1<u:
#             print(l,u)
#             mid = (l+u)//2
#             print('mid',mid)
#             add = 0
#             for i in range(len(nums)):
#                 add = add + math.ceil(nums[i]/mid)
#             print(add)

#             if add>threshold:
#                 l = mid
#             elif add == threshold:
#                 return mid
#             else:
#                 addl.append(mid)
#                 u = mid

#         return min(addl
