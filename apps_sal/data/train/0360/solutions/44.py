class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (lo, hi) = (0, 9999999)
        ans = -1
        N = len(weights)
        for w in weights:
            lo = max(lo, w)

        def poss(val):
            (n, cnt, sum) = (0, 1, 0)
            while n < N:
                if sum + weights[n] <= val:
                    sum += weights[n]
                else:
                    cnt += 1
                    sum = weights[n]
                n += 1
            return cnt
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            nn = poss(mid)
            if nn <= D:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
