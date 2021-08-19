class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed))
        times = [float(target - p) / s for (p, s) in pos_speed]
        res = 0
        cur = 0
        for t in times[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res
