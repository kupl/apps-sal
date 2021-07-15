class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(days) -> bool:
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m

        if len(bloomDay) < m * k:
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         def feasible(day):
#             adj_count = 0
#             bouquet = 0
#             for bday in bloomDay:
#                 if bday <= day:
#                     adj_count += 1
#                 else:
#                     adj_count = 0
#                 if adj_count == k:
#                     bouquet += 1
#                     adj_count = 0
#             return bouquet == m
        
#         if len(bloomDay) < m * k:
#             return -1
#         left, right = 1, max(bloomDay)
#         while left < right:
#             mid = (left + right) // 2
#             if feasible(mid):
#                 right = mid
#             else:
#                 left = mid + 1
#         return left

