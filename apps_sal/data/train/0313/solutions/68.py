class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k>n: return -1
        
        def canmake(days):
            flowers=0
            bs=0
            i=0
            while bs<m and i<n:
                while flowers<k and i<n:
                    if bloomDay[i]<=days:
                        flowers+=1
                    else:
                        flowers=0
                    i+=1
                if flowers==k:
                    flowers=0
                    bs+=1
            return bs==m
        
        l,r=min(bloomDay),max(bloomDay)
        
        while l<r:
            mid=(l+r)>>1
            if canmake(mid):
                r=mid
            else:
                l=mid+1
        return l
