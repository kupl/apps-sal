class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         binary search
        def validable(days):
#             how many booms in days, and how many bouquet can make
            bloom = 0
            bouquet = 0
            for b in bloomDay:
                if b <= days:
                    bloom += 1
                    bouquet += bloom // k
                    bloom = bloom % k
                else:
                    bloom = 0
            return bouquet >= m
                    
        if len(bloomDay) < m * k:
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if validable(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    
    
#     def minDays(bloomDay: List[int], m: int, k: int) -> int:
#     def feasible(days) -> bool:
#         bonquets, flowers = 0, 0
#         for bloom in bloomDay:
#             if bloom > days:
#                 flowers = 0
#             else:
#                 bonquets += (flowers + 1) // k
#                 flowers = (flowers + 1) % k
#         return bonquets >= m

#     if len(bloomDay) < m * k:
#         return -1
#     left, right = 1, max(bloomDay)
#     while left < right:
#         mid = left + (right - left) // 2
#         if feasible(mid):
#             right = mid
#         else:
#             left = mid + 1
#     return left

