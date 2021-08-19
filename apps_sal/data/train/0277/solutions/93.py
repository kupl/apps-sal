class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        _max = 0
        _min = 1
        num_moments = 0
        for i in range(len(light)):
            if _max < light[i]:
                _max = light[i]
            if _max - _min == i:
                num_moments += 1
        return num_moments
