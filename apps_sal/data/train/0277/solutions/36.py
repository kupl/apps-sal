class Solution:

    def numTimesAllBlueQuad(self, light: List[int]) -> int:
        blue = 0
        lights = [0 for l in light]
        for l in light:
            lights[l - 1] = 1
            if all([x == 1 for x in lights[:l - 1]]):
                blue += 1
                print(l)
        return blue

    def numTimesAllBlue(self, light: List[int]) -> int:
        count = 0
        sums = [0] * (len(light) + 1)
        for (idx, l) in enumerate(light):
            sums[idx + 1] = sums[idx] + l
        print(sums)
        for (idx, l) in enumerate(light):
            if sums[idx + 1] == self.required(idx + 1):
                count += 1
        return count

    @staticmethod
    def required(n):
        return (n + 1) * n // 2
