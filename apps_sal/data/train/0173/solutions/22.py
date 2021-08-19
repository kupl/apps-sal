from collections import defaultdict


class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        n: int = len(arr)
        mods = {ix: 0 for ix in range(k)}
        for val in arr:
            mods[val % k] += 1
        if mods[0] % 2 != 0:
            return False
        for mod in range(1, k):
            comp = k - mod
            if mods[comp] != mods[mod]:
                return False
        return True
