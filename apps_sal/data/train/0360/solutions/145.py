class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (r - l) // 2 + l
            day = self.weightWhetherWork(weights, mid)
            if day > D:
                l = mid + 1
            else:
                r = mid
        return l

    def weightWhetherWork(self, weights, mid):
        temp = mid
        day = 1
        for i in weights:
            if temp >= i:
                temp -= i
            else: 
                temp = mid
                temp -= i
                day += 1
        return day
