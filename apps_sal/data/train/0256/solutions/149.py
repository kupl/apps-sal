class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def K_speed(K, piles):
            hours_to_eat = 0
            for pile in piles:
                hours_to_eat = hours_to_eat + pile // K
                if pile % K != 0:
                    hours_to_eat += 1
            return hours_to_eat
        left = 1
        right = max(piles)
        while left < right:
            K = left + (right - left) // 2
            if K_speed(K, piles) <= H:
                right = K
            else:
                left = K + 1
        return left
