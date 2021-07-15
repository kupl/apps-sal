class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        lo = 1
        hi = 10**18
        position.sort()
        def func(mid):
            cnt = 1
            cur = position[0]
            for i in range(1,len(position)):
                if position[i]>=cur+mid:
                    cur = position[i]
                    cnt+=1
            if cnt>=m:
                return True
            else:
                return False
            
        while lo<hi:
            mid = (lo+hi)//2
            x = func(mid)
            if x==True:
                lo = mid
            else:
                hi = mid
            if hi-lo==1:
                break
        if func(hi)==True:
            return hi
        return lo
            

