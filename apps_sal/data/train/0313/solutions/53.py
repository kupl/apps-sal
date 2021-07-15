class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def canMakeMBouquetsInKDays(max_days):
            flowers = 0
            bouquets = 0
            for flower in range(len(bloomDay)):
                if bloomDay[flower]<=max_days:
                    flowers+=1
                else:
                    flowers=0  
                if flowers==k:
                    bouquets+=1
                    flowers=0
                if bouquets==m:
                    return True
            return bouquets>=m
            
        
        if m*k>len(bloomDay):
            return -1
        
        start = 1
        end = max(bloomDay)
        while start<=end:
            mid = (start+end)//2
            if canMakeMBouquetsInKDays(mid):
                end = mid-1
            else:
                start = mid+1
        return start
