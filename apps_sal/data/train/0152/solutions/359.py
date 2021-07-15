class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        
        def count(d):
            cnt = 1
            cur = position[0]
            for p in position[1:]:
                if p>=cur+d: cur, cnt = p, cnt+1
            return cnt
        
        l, r = 0, position[-1]-position[0]
        while l<r:
            mid = r - (r-l)//2
            # count_mid = count(mid)
            # if count(mid) >= m: return r-l
            if count(mid) < m:
                r = mid-1 
            else:
                l = mid
            # print(mid, count(mid))
        return r
            
        
        
        
                    

