class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(w):
            i = 0
            for day in range(D):
                ship_w = 0
                while i < len(weights):
                    # print(str(w - ship_w)+\">=\"+str(weights[i]))
                    if w - ship_w >= weights[i]:
                        ship_w += weights[i]
                    else:
                        break
                    i += 1
            return i == len(weights)
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) >> 1
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
