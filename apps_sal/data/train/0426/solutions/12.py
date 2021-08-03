from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:

        Nstr = str(N)
        pset = set(''.join(p) for p in permutations(Nstr))

        bmk = 1
        while len(str(bmk)) < len(Nstr):
            bmk *= 2

        while len(str(bmk)) == len(Nstr):
            if str(bmk) in pset:
                return True
            bmk *= 2

        return False
