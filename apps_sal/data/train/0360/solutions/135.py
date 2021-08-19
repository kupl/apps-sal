class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)

        def calc(cap):
            cnt = 0
            cur = 0
            for w in weights:
                cur += w
                if cur > cap:
                    cur = w
                    cnt += 1
            return cnt + 1 <= D
        while l < r:
            mid = (l + r) // 2
            good = calc(mid)
            if good:
                r = mid
            else:
                l = mid + 1
        return l
