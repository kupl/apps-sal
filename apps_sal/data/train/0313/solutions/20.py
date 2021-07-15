class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k*m > len(bloomDay): 
            return -1
        
        def isPossible(mid): 
            numFlowers = 0
            numBouquets = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > mid:
                    numFlowers = 0
                else:
                    numFlowers += 1
                    if numFlowers >= k:
                        numBouquets += 1
                        numFlowers -= k
            
            # print(mid, numBouquets)
            return numBouquets >= m
        
        low = 0
        high = max(bloomDay)
        while (low < high):
            mid = int((low + high)/2)
            if (isPossible(mid)):
                # print(\"true\", mid)
                high = mid
            else:
                low = mid + 1
        return low 
                
            

