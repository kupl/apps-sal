class Solution:

    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_num = minutes / 5
        hour += minutes / 60
        angle = abs(hour - minutes_num) * 30
        return min(360 - angle, angle)
