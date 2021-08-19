class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def check_possible(capacity):
            count = 0
            i = 0
            while i < len(weights):
                count += 1
                if count > D or weights[i] > capacity:
                    return False
                curr_ship = 0
                while i < len(weights) and weights[i] + curr_ship <= capacity:
                    curr_ship += weights[i]
                    i += 1
            return True
        tot = 0
        largest = 0
        for w in weights:
            tot += w
            largest = max(largest, w)
        l = largest
        r = tot
        if check_possible(l):
            return l
        while l < r - 1:
            mid = (l + r) // 2
            if check_possible(mid):
                r = mid
            else:
                l = mid
        return r
