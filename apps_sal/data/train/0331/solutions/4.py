class Solution:

    def angleClock(self, hour: int, minutes: int) -> float:
        hr = (hour + float(minutes / 60)) * 30
        mi = minutes * 6
        ang = abs(hr - mi)
        return min(360.0 - ang, ang)
