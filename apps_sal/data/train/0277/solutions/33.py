class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        (yellow, blue) = (set(), set())
        moment = 0
        for bulb in light:
            if bulb == 1 or bulb - 1 in blue:
                blue.add(bulb)
                t = bulb + 1
                while t in yellow:
                    yellow.remove(t)
                    blue.add(t)
                    t += 1
            else:
                yellow.add(bulb)
            if not yellow:
                moment += 1
        return moment
