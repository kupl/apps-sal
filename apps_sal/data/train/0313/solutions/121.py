class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        minDays = float('inf')
        maxDays = 0
        for bloomday in bloomDay:
            if (bloomday < minDays):
                minDays = bloomday
            if (bloomday > maxDays):
                maxDays = bloomday

        low = minDays
        high = maxDays
        mid = (low+high)//2

        while (low < high):
            if(self.validDays(mid, bloomDay, m, k)):
                high = mid
            else:
                low = mid+1
            mid = (low+high)//2

        if (self.validDays(low, bloomDay, m, k)):
            return low
        return -1

    def validDays(self, days, bloomDay, m, k):
        bouquets = 0
        idx = 0
        while(idx < len(bloomDay)):
            flowergroupcount = 0
            while (idx < len(bloomDay) and bloomDay[idx] <= days):
                flowergroupcount += 1
                idx += 1
            bouquets += flowergroupcount//k
            idx += 1
        if (bouquets >= m):
            return True
        return False
