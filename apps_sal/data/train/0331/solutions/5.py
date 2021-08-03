class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # calculate the angle for hour and minutes separately and then calculate the min
        minute_angle = 360 / 60 * minutes
        hour_angle = (hour % 12) * (360 / 12) + ((minutes / 60) * (360 / 12))
        return min(abs(hour_angle - minute_angle), 360 - abs(hour_angle - minute_angle))
