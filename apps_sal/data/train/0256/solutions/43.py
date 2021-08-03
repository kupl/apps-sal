class Solution:
    def hours(self, piles, k):
        cnt = 0
        for p in piles:
            if p <= k:
                cnt = cnt + 1
            else:
                cnt = cnt + p // k + 1
        return cnt

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) == 1:
            return 1 + piles[0] // H
        l = 0
        r = max(piles)
        while(l <= r):
            mid = (l + r) // 2
            hrs = self.hours(piles, mid)
            if (hrs <= H):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
