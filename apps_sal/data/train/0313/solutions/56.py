class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(day):
            numAdjFlowers = 0
            numBouquets = 0
            
            for bloom in bloomDay:
                if bloom <= day:
                    numAdjFlowers += 1
                    if numAdjFlowers == k:
                        numBouquets += 1
                        numAdjFlowers = 0
                else:
                    numAdjFlowers = 0
            return numBouquets >= m
                    
        # Eliminate cases where it's not possible
        if len(bloomDay) < (m*k):
            return -1
                    
        left = min(bloomDay)
        right = max(bloomDay)
        
        while left < right:
            mid = left + (right - left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
