class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        min_speed = 1
        max_speed = sorted(piles)[-1]
        while min_speed <= max_speed:
            # print('min_speed',min_speed)
            # print('max_speed',max_speed)

            pivot = min_speed + (max_speed - min_speed) // 2
            # print('current_speed',pivot)

            hours = [math.ceil(x / pivot) for x in piles]
            # print('hours=',hours)
            r = 0
            for x in hours:
                if x == 0:
                    # print('if_x',x+1)
                    r += 1
                else:
                    # print('else_x',x)
                    r += x
            # print('r',r)
            # print()
            if r == H:
                return pivot
            elif min_speed == max_speed and r >= H:
                return pivot + 1
            # elif min_speed==max_speed and r < H:
            #    min_speed = pivot+1
            elif r < H:
                max_speed = pivot - 1

            elif r > H:
                min_speed = pivot + 1
        return pivot
