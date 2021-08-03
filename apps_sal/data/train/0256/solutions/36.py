class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Find the first <= in  [> > > > > <= <=]
        n = len(piles)
        low, high = 1, max(piles)
        while (low + 1) < high:
            mid = low + ((high - low) // 2)
            used_hrs = self.calc_hours(piles, mid)
            #print(mid, used_hrs)
            if used_hrs > H:
                low = mid
            else:
                high = mid

        if self.calc_hours(piles, low) <= H:
            return low
        if self.calc_hours(piles, high) <= H:
            return high

    @staticmethod
    def calc_hours(piles, K):
        return int(sum(math.ceil(pile / float(K)) for pile in piles))
