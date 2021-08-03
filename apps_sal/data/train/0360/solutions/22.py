class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        lo = max(weights)
        hi = sum(weights)

        def calculate_capacity(n):
            num_day = 1
            curr_capacity = 0
            for weight in weights:
                if curr_capacity + weight <= n:
                    curr_capacity += weight
                else:
                    num_day += 1
                    curr_capacity = weight
            return num_day

        while lo < hi:
            mid = lo + (hi - lo) // 2
            day = calculate_capacity(mid)
            if day > D:
                lo = mid + 1
            else:
                hi = mid
        return lo
