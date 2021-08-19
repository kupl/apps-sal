class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) / 12 * 360 + (minutes / 60) * 30
        min_angle = minutes / 60 * 360
        target = abs(hour_angle - min_angle)
        #print (hour_angle, min_angle)
        if target > 180:
            target = 360 - target
        return target
