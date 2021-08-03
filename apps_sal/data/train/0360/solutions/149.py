class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid, load, need = (left + right) // 2, 0, 1
            for w in weights:
                load += w
                if load > mid:
                    need += 1
                    load = w
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left
