from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        mods = [0]
        modFreqs = defaultdict(lambda: 0)
        for num in nums:
            mod = (mods[-1] + num) % k
            if mod == 0:
                count += 1
            count += modFreqs[mod]
            mods.append(mod)
            modFreqs[mod] += 1
        return count
