class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        _min = len(light) + 1
        _max = 0
        missing = set()
        num_moments = 0

        for i in light:
            if i > _max:
                if _max != 0:
                    for j in range(_max + 1, i):
                        missing.add(j)
                _max = i
            if i < _min:
                if _min != len(light) + 1:
                    for j in range(i + 1, _min):
                        missing.add(j)
                _min = i
            if i in missing:
                missing.remove(i)
            if len(missing) == 0 and _min < 2:
                num_moments += 1
        return num_moments
