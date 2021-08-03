class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def is_valid(speed):
            curr = 0
            for n in piles:
                q, r = divmod(n, speed)
                if r:
                    q += 1
                curr += q
                if curr > H:
                    return False
            return True

        l, r = 1, max(piles)
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
