class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        prof = rots = wait = 0
        maxp = float('-inf')
        maxr = -1
        for c in customers:
            rots += 1
            wait += c
            ride = min(wait, 4)
            wait -= ride
            prof += ride * boardingCost - runningCost
            if maxp < prof:
                maxp = prof
                maxr = rots
        while wait > 0:
            rots += 1
            ride = min(wait, 4)
            wait -= ride
            prof += ride * boardingCost - runningCost
            if maxp < prof:
                maxp = prof
                maxr = rots
        return maxr if maxp > 0 else -1
