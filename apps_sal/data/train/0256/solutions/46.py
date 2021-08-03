class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo = 1
        hi = max(piles)
        ans = 0
        while hi >= lo:
            mid = (lo + hi) // 2
            if self.check(mid, piles, H):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans

    def check(self, mid, piles, H):
        i = 0
        count = 0
        new = piles[::]
        while i < len(new):
            if count > H:
                return False
            if mid >= new[i]:
                count += 1
                i += 1
            else:
                count += new[i] // mid + 1
                i += 1
        if count > H:
            return False
        return True
