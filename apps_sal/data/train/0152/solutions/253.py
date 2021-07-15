class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        n = len(pos)
#         def check(gap):
#             i = 0
#             ii = 0
#             nn = 1
#             while i < n:
#                 if pos[i] - pos[ii] >= gap:
#                     nn += 1
#                     ii = i
#                 i += 1
#             return nn >= m
        
#         l = 1
#         r = 10 ** 9
        
#         while l < r:
#             mid = (l + r + 1) // 2
#             if check(mid):
#                 l = mid
#             else:
#                 r = mid - 1 
#         return l
    
        def isNotOK(gap):
            i = 0
            ii = 0
            nn = 1
            while i < n:
                if pos[i] - pos[ii] >= gap:
                    nn += 1
                    ii = i
                i += 1
            return nn < m
        
        l = 1
        r = 10 ** 9
        
        while l < r:
            mid = (l + r) // 2
            if isNotOK(mid):
                r = mid
            else:
                l = mid + 1 
        return l - 1
            

