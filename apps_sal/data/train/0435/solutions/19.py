class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cumsum = 0
        complements = {0: 1}
        counts = 0
        for a in A:
            cumsum += a
            mods = cumsum % K
            counts += complements.get(mods, 0)
            complements[mods] = complements.get(mods, 0) + 1
        return counts
