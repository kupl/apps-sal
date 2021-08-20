class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lower = max(weights)
        upper = sum(weights)
        while abs(lower - upper) > 1:
            mid = (lower + upper) // 2
            if self.is_shipped(mid, weights, D):
                upper = mid
            else:
                lower = mid
        if lower == upper or self.is_shipped(lower, weights, D):
            return lower
        else:
            return upper

    def is_shipped(self, cap, weights, D):
        tmp = 0
        count = 1
        for i in range(len(weights)):
            tmp += weights[i]
            if tmp == cap:
                count += 1
                tmp = 0
            elif tmp > cap:
                count += 1
                tmp = weights[i]
        return count <= D
