from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:

        if N == 1:
            return True

        Nstr = str(N)
        pset = set(''.join(p) for p in permutations(Nstr) if int(p[-1]) % 2 == 0)

        bmk = 1
        while len(str(bmk)) < len(Nstr):
            bmk *= 2

        while len(str(bmk)) == len(Nstr):
            if str(bmk) in pset:
                return True
            bmk *= 2

        return False
