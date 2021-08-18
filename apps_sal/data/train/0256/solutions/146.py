class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def eat_speed(K, H):
            banana_per_hour = 0
            for pile in piles:
                banana_per_hour += pile // K
                if pile % K != 0:
                    banana_per_hour += 1
            return banana_per_hour

        left = 1
        right = max(piles)

        while left <= right:
            K = left + (right - left) // 2
            banana_per_hour = eat_speed(K, H)
            if banana_per_hour <= H:
                right = K - 1
            else:
                left = K + 1
        return left
