class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        for m, n in zip(s1, s2):
            if m == 'x' and n == 'y':
                xy += 1
            elif m == 'y' and n == 'x':
                yx += 1

        if (xy + yx) % 2 != 0:
            return -1
        else:
            return xy // 2 + yx // 2 + xy % 2 + yx % 2
