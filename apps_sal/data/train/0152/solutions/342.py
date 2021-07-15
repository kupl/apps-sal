class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        n = len(pos)
        def check(gap):
            i = 0
            ii = 0
            nn = 1
            while i < n:
                if pos[i] - pos[ii] >= gap:
                    nn += 1
                    ii = i
                i += 1
            return nn < m
        
        l = float('inf')
        for i in range(n-1):
            l = min(l, pos[i+1] - pos[i])
        r = pos[-1] - pos[0] + 1
        
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l - 1
#         if check(l):
#             return l
#         else:
#             return l - 1
            

