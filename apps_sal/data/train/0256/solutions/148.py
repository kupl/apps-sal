class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def count_hours(k):
            hours = 0
            if k == 1:
                return sum(piles)
            for p in piles:
                hours += p//k
                if p%k != 0:
                    hours += 1
            return hours
        least = 1
        most = max(piles)
        
        while least <= most:
            mid = (most+least)//2
            num_hours = count_hours(mid)
            if num_hours <= H:
                most = mid -1
            else:
                least = mid + 1
        return least

