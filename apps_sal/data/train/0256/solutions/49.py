class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        min_speed = 1
        max_speed = sorted(piles)[-1]
        while min_speed <= max_speed:

            pivot = min_speed + (max_speed - min_speed) // 2

            hours = [math.ceil(x / pivot) for x in piles]
            r = 0
            for x in hours:
                if x == 0:
                    r += 1
                else:
                    r += x
            if r == H:
                return pivot
            elif min_speed == max_speed and r >= H:
                return pivot + 1
            elif r < H:
                max_speed = pivot - 1

            elif r > H:
                min_speed = pivot + 1
        return pivot
