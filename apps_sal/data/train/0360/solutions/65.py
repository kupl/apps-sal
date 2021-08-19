class Solution:

    def canShip(self, w, d, cap):
        i = 0
        res = 0
        while i < len(w):
            if w[i] > cap:
                return False
            remain = cap
            while i < len(w) and remain >= w[i]:
                remain -= w[i]
                i += 1
            res += 1
        return res <= d

    def shipWithinDays(self, w: List[int], D: int) -> int:
        if len(w) == 0:
            return 0
        start = max(w)
        end = sum(w)
        while start < end:
            mid = int((end - start) / 2) + start
            if self.canShip(w, D, mid):
                end = mid
            else:
                start = mid + 1
        return start
