class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def is_possible(C):
            if C < max(weights):
                return False

            d, i, cap, n = 1, -1, 0, len(weights)
            while d <= D:
                while i < n - 1 and cap + weights[i + 1] <= C:
                    cap += weights[i + 1]
                    i += 1
                d += 1
                cap = 0
            if i < n - 1:
                return False
            return True

        left, right = 0, sum(weights)
        while left < right:
            mp = left + (right - left) // 2
            if is_possible(mp):
                right = mp
            else:
                left = mp + 1

        return left
