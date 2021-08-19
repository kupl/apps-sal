class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = sum((x - 1) // mid + 1 for x in piles)  # 从1开始需要-1
            if hours <= H:  # mid越大 ，需要时间越短
                right = mid - 1
            else:
                left = mid + 1
        return left


#         def hours(k):
#             count = 0
#             for x in piles:
#                 count += (x-1)//k + 1
#             return count

#         left = 1
#         right = max(piles)
#         while left <= right:
#             mid = (left + right)//2
#             if hours(mid) <= H:  #
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return left


#         def hours(k):
#             h = 0
#             for x in piles:
#                 h += (x-1)//k + 1
#             return h

#         left = 1
#         right = max(piles)  # 最多也就是每次都吃完
#         while left <= right:
#             mid = (left + right)//2
#             if hours(mid) > H:
#                 left = mid + 1
#             else:
#                 right = mid -1
#         return left


#         def hours(k):
#             h = 0
#             for x in piles :
#                 h += (x-1)//k + 1
#             return h

#         left = 1
#         right = max(piles)
#         while left <= right:
#             mid = (left + right)//2
#             if hours(mid) <= H:
#                 right = mid - 1
#             else: left = mid + 1
#         return left
