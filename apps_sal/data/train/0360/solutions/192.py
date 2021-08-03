class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        weights_sum = sum(weights)

        def necessary_days(capacity):
            days = 0
            ws = 0
            for w in weights:
                if ws + w <= capacity:
                    ws += w
                else:
                    days += 1
                    ws = w

            return days + 1

        low = max(weights)
        high = weights_sum
        capacity_guess = (low + high) // 2

        while low <= high:
            d = necessary_days(capacity_guess)

            if d <= D:
                high = capacity_guess - 1
            else:
                low = capacity_guess + 1

            capacity_guess = (low + high) // 2

        return low
