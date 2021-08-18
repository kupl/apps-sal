class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if(hour <= 6):
            originaldiff = hour * 30 * -1
        else:
            originaldiff = (12 - hour) * 30
        print(originaldiff)
        mintravelled = 5.5 * minutes
        return min(abs(mintravelled + originaldiff), abs(mintravelled + originaldiff - 360))
