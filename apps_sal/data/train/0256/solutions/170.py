class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        while min_speed <= max_speed:
            pivot = min_speed + (max_speed - min_speed) // 2
            r = sum([math.ceil(x / pivot) for x in piles])
            if r == H:
                return pivot
            elif min_speed == max_speed and r >= H:
                return pivot + 1
            elif r < H:
                max_speed = pivot - 1
            elif r > H:
                min_speed = pivot + 1

        return pivot
