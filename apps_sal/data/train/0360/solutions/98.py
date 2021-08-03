class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        cap_min = max(weights)
        cap_max = sum(weights)

        # binary search the minimum cap

        while cap_min < cap_max:
            cap_mid = (cap_min + cap_max) // 2

            days = self._cal_num_of_days(weights, cap_mid)

            if days > D:
                cap_min = cap_mid + 1
            elif days < D:
                cap_max = cap_mid
            elif days == D:
                cap_max = cap_mid

        return cap_min

    def _cal_num_of_days(self, weights: List[int], cap: int) -> int:
        days = 0
        i = 0

        while i < len(weights):
            current_load = 0
            while i < len(weights) and current_load + weights[i] <= cap:
                current_load += weights[i]
                i += 1
            days += 1
        return days
