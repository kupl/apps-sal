import numpy as np
import itertools as it


class Solution:
    # #     def maxDistance(self, position: List[int], m: int) -> int:
    #         arr = np.sort(position)
    #         md = max(arr)
    #         # print(arr)

    #         combList = list(it.combinations(arr, m))
    #         # print(combList)
    #         maxmindiff = 0
    #         targetList = []
    #         for comb in combList:
    #             cb = list(it.combinations(comb, 2))
    #             minDiff = md
    #             for k in range(len(cb)):
    #                 curDiff = abs(cb[k][0]-cb[k][1])
    #                 if curDiff< minDiff:
    #                     minDiff= curDiff

    #             if minDiff>maxmindiff:
    #                 maxmindiff = minDiff
    #                 targetList = comb
    #         # print(maxmindiff)
    #         # print(targetList)
    #         return maxmindiff

    def maxDistance(self, position: List[int], m: int) -> int:
        arr = np.sort(position)
        arr = arr - np.min(arr)
        print(arr)

        def isFeasible(mid, arr, m):
            pos = arr[0]
            n = len(arr)
            count = 1
            for i in range(n):
                if arr[i] - pos >= mid:
                    pos = arr[i]
                    count += 1
                if count >= m:
                    return True
            return False

        left = arr[0]
        right = arr[-1]

        if m == 2:
            return right - left
        res = -1
        count = 0
        while left < right:
            # mid = np.ceil((right+left)/2)
            mid = (right + left) // 2
            # mid = right-(right-left)//2
            # print(mid)
            count += 1
            if isFeasible(mid, arr, m):
                res = max(res, mid)
                left = mid + 1

            else:
                right = mid
        print(count)
        return int(res)

# 3
# class Solution:
#     def maxDistance(self, position: List[int], m: int) -> int:
#         n = len(position)
#         position.sort()

#         def count(d):
#             ans, curr = 1, position[0]
#             for i in range(1, n):
#                 if position[i] - curr >= d:
#                     ans += 1
#                     curr = position[i]
#             return ans

#         l, r = 0, position[-1] - position[0]
#         while l < r:
#             mid = r - (r - l) // 2
#             if count(mid) >= m:
#                 l = mid
#             else:
#                 r = mid - 1
#         return l
