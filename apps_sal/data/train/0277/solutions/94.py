class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        moment = 0
        bulbsOn = 0
        for i in range(len(light)):
            bulbsOn = max(bulbsOn, light[i])
            if bulbsOn == i + 1:
                moment += 1
        return moment
