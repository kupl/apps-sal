class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        if not weights:
            return 0

        NUM_PACKAGES = len(weights)
        if NUM_PACKAGES == 1:
            return weights[0]
        elif NUM_PACKAGES == 2:
            return max(weights[0], weights[1])

        max_capacity, min_capacity = 0, 0
        for weight in weights:
            max_capacity += weight
            min_capacity = weight if weight > min_capacity else min_capacity

        def possible(capacity):
            curr_weight = 0
            curr_days = 0
            package_index = 0

            while package_index < NUM_PACKAGES:

                if curr_weight + weights[package_index] > capacity:
                    curr_days += 1

                    if curr_days > D:
                        return False

                    curr_weight = 0

                curr_weight += weights[package_index]
                package_index += 1

            curr_days += 1
            if curr_days > D:
                return False

            return True

        least_capacity = 0
        while min_capacity <= max_capacity:
            mid_point = (min_capacity + max_capacity) // 2
            if possible(mid_point):
                least_capacity = mid_point
                max_capacity = mid_point - 1
            else:
                min_capacity = mid_point + 1

        return least_capacity
