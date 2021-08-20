class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        (lo, hi) = (1, 1000000001)
        ans = -1
        N = len(piles)

        def poss(val):
            cnt = 0
            for n in range(N):
                cnt += math.ceil(piles[n] / val)
            if cnt <= H:
                return True
            return False
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if poss(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
