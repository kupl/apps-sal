class Solution:

    def minEatingSpeed(self, piles, H):
        speed = math.floor(sum(piles) / H)
        while True:
            time = sum([math.ceil(x / speed) if speed else float('inf') for x in piles])
            print(f'speed={speed!r}, time={time!r}, H={H!r}')
            if time <= H:
                break
            speed += 1
        return speed
