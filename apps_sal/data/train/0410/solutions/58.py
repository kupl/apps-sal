class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powerSteps = []
        for i in range(lo, hi + 1):
            powerSteps.append((self.getPowerSteps(i), i))
        powerSteps.sort()
        return powerSteps[k - 1][1]
        
        
    def getPowerSteps(self, value):
        steps = 0
        while value != 1:
            if value % 2 == 0:
                value = value / 2
            else:
                value = 3 * value + 1
            steps += 1
        return steps
