class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_light = 0
        num = 0
        res = 0
        for i, l in enumerate(light):
            max_light = max(max_light, l)

            print(max_light)
            if i + 1 >= max_light:
                res += 1
        return res
