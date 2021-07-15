class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ###weirdly not working :(
        n = len(position)
        position.sort()
        res = 0
        
        def feasible(distance):
            balls, curr = 1, position[0]
            for i in range(1, n):
                if position[i]-curr >= distance+1:
                    balls += 1
                    curr = position[i]                    
            return balls >= m
                           
        left, right = 0, position[-1]-position[0]
        while left<right:
            mid = left + (right-left)//2
            if feasible(mid):
                left = mid+1
            else:
                right = mid
        return left

#         n = len(position)
#         position.sort()
        
#         def count(d):
#             ans, curr = 1, position[0]
#             for i in range(1, n):
#                 if position[i] - curr >= d:
#                     ans += 1
#                     curr = position[i]
#             return ans >= m
        
#         l, r = 0, position[-1] - position[0]
#         while l < r:
#             mid = r - (r - l) // 2   ###speed_up
#             # mid = l + (r-l)//2  ###TLE
#             if count(mid):
#                 l = mid
#             else:
#                 r = mid - 1
#         return l

