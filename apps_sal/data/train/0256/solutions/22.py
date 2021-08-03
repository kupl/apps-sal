
class Solution:
    def minEatingSpeed(self, piles, H):
        speed = math.floor(sum(piles) / H)
        while True:
            time = sum([math.ceil(x / speed) if speed else float('inf') for x in piles])
            print(f'{speed=}, {time=}, {H=}')
            if time <= H:
                break
            speed += 1
        return speed
