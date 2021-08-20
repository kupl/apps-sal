class Solution:

    def angleClock(self, hour: int, minutes: int) -> float:
        angle_per_min = 360 / 60
        angle_per_5_min = 5 * angle_per_min
        h = hour % 12 + minutes / 60
        hr_angle = h * angle_per_5_min
        min_angle = minutes * angle_per_min
        r = abs(hr_angle - min_angle)
        return min(360 - r, r)
