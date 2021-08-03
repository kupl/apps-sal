class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:

        maxBulb = 0
        maxBlue = 0
        count = 0

        moments = [False for i in range(len(light))]
        for idx, bulb in enumerate(light):
            maxBulb = max(maxBulb, bulb)
            moments[bulb - 1] = True
            if bulb == 1 or maxBlue == bulb - 1:
                maxBlue = bulb
                i = bulb + 1
                while(i <= len(light) and moments[i - 1]):
                    maxBlue = i
                    i += 1

            if maxBlue == maxBulb:
                count += 1
        return count
