class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def is_power_of_two(c):
            return bin(int(''.join(c))).count('1') == 1
        permutations = itertools.permutations(str(N))
        for cand in permutations:
            if cand[0] != '0' and is_power_of_two(cand):
                return True

        return False
