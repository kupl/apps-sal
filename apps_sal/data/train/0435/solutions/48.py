class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:

        cumsum = 0
        counts = 0
        complements = {0: 1}
        for a in A:
            cumsum += a
            mods = cumsum % K
            counts += complements.get(mods, 0)
            complements[mods] = complements.get(mods, 0) + 1

        return counts
