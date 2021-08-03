class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def test(capacity):
            count = 0
            current_sum = 0
            i = 0

            while i < len(weights) and count < D:
                while i < len(weights) and current_sum + weights[i] <= capacity:
                    current_sum += weights[i]
                    i += 1

                count += 1
                current_sum = 0

            return count <= D and i == len(weights)

        l, r = 1, sum(weights)

        while l < r:
            mid = (l + r) // 2

            if test(mid):
                r = mid
            else:
                l = mid + 1

        return l
