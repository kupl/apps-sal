class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        total = sum(weights)
        lo,hi = max(max(weights),total//D), total
        n=len(weights)
        def valid(x):
            i = days = 0
            while i < n:
                S=0
                while i<n and S+weights[i]<=x:
                    S+=weights[i]
                    i+=1
                days+=1
            return days<=D
        
        while lo<hi:
            mid = (lo+hi)//2
            print(mid)
            if valid(mid):
                hi=mid
            else:
                lo=mid+1
        return lo
                    

