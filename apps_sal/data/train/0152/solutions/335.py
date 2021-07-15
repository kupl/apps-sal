class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
#         def feasible(distance):
#             balls, curr = 1, position[0]
#             for i in range(1, len(position)):
#                 if position[i]-curr >= distance:
#                     balls += 1
#                     curr = position[i]
                    
#             return balls >= m
            
        
#         position.sort()
#         left, right = 0, position[-1]-position[0]
#         while left<right:
#             mid = left + (right-left)//2
#             if feasible(mid):
#                 right = mid
#             else:
#                 left = mid+1
#         return left

        n = len(position)
        position.sort()
        
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

