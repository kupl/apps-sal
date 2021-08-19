class Solution:

    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = hour * 30 + minutes / 12 * 6
        if hour_angle > 360:
            hour_angle -= 360
        min_angle = minutes / 5 * 30
        if min_angle > 360:
            min_angle -= 360
        diff = abs(hour_angle - min_angle)
        return diff if diff <= 360 - diff else 360 - diff
