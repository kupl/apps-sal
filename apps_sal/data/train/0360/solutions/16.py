class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lower = min(weights)
        upper = sum(weights)

        while lower < upper:
            mid = (lower + upper) // 2
            if self.check(weights, D, mid):
                upper = mid
            else:
                lower = mid + 1

        return lower

    def check(self, weights, D, cap):
        s = weights[0]
        ct = 1
        if s > cap:
            return False

        for x in weights[1:]:
            if x > cap:
                return False
            if s + x <= cap:
                s += x
            else:
                s = x
                ct += 1
        return ct <= D
