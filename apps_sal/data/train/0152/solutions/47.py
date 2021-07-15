class Solution:
    def maxDistance(self, pos: [int], m: int) -> int:
        pos.sort()
        N = len(pos)
        
        high = (pos[-1]-pos[0])//(m-1)
        low = 1
        
        def check(dist):
            cnt = 1
            loc = pos[0]
            for i in range(1, N):
                if pos[i]-loc>=dist:
                    cnt += 1
                    loc = pos[i]
                    if cnt == m:
                        return True
            return False
        
        while high!=low:
            mid = (high+low+1)//2
            if check(mid):
                low = mid
            else:
                high = mid-1
        
        return high
                
        
        
            
        

