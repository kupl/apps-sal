class Solution:
    def search(self, bloomDay, m, k, days):
        bouquets = 0
        flowers = 0
        for day in bloomDay:
            if day > days:
                flowers = 0
            else:
                bouquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
               
        return bouquets >= m
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        lowerBound = 1
        upperBound = max(bloomDay)
        
        while lowerBound <= upperBound:
            mid = (lowerBound + upperBound) // 2
            check = self.search(bloomDay, m, k, mid)
            if check:
                upperBound = mid - 1
            else:
                lowerBound = mid + 1
        return lowerBound
