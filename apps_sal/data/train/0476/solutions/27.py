class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        pos_spd = sorted(zip(position, speed))
        position = [x for (x, y) in pos_spd]
        speed = [y for (x, y) in pos_spd]
        time = list([(target - x[0]) / x[1] for x in pos_spd])
        idx = []
        count = 1
        temp = time[-1]
        for val in time[::-1]:
            if val > temp:
                count += 1
                temp = val
        return count
