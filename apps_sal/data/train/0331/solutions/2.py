class Solution:

    def angleClock(self, hour: int, minutes: int) -> float:
        hour = hour if hour < 12 else hour - 12
        minute_angle = float(minutes) / 60.0 * 360.0
        hour_angle = 30.0 * hour + minutes / 60 * 360.0 / 12.0
        return abs(minute_angle - hour_angle) if abs(minute_angle - hour_angle) < 180.0 else 360.0 - abs(minute_angle - hour_angle)
