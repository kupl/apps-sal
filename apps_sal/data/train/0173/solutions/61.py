from collections import Counter


class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = [x % k for x in arr]
        cMods = Counter(mods)
        totalP = 0
        for cm in cMods:
            if cm == 0 or cMods[cm] == 0:
                totalP += cMods[cm]
                continue
            if cMods[cm] != cMods[k - cm]:
                return False
        if cMods[0] % 2 == 0:
            return True
        else:
            return False
