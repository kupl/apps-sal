class Solution:

    def get_hours(self, piles, k):
        ans = 0
        for x in piles:
            if x % k == 0:
                ans += x // k
            else:
                ans += int(x // k) + 1
        return ans

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        (n, max_val) = (len(piles), max(piles))
        if H < n:
            return 1 << 31
        (start, end) = (1, max_val)
        while start <= end:
            mid = (end - start) // 2 + start
            h = self.get_hours(piles, mid)
            if h <= H:
                end = mid - 1
            else:
                start = mid + 1
        return start if start <= max_val else start - 1
