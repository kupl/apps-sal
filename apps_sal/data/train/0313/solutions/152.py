class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def checkFlowers(mid,m,k):
            bq = 0
            i = 0
            while i <len(bloomDay):
                if bloomDay[i] <= mid:
                    count = 1
                    i+=1
                    while i <len(bloomDay) and count < k and bloomDay[i] <= mid:
                        count+=1
                        i+=1
                    if count == k:
                        bq+=1
                else:
                    i+=1
            return bq
        
        
        if len(bloomDay) < k*m :
            return -1
        
        low = 1
        high = max(bloomDay)
        while low < high:
            mid = (low + high)//2
            x = checkFlowers(mid,m,k) 
            if x >= m:
                high = mid
            else:
                low = mid + 1
        return high
