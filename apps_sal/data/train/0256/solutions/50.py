class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def cnt(k, piles):
            ans = 0
            for p in piles:
                ans += math.ceil(p / float(k))
            return int(ans)
        piles.sort()
        l = 1
        h = piles[-1]
        mid = (l + h) // 2
        while l <= h:
            s = cnt(mid, piles)
            if s <= H:
                h = mid - 1
            else:
                l = mid + 1
            mid = (l + h) // 2
        return l
