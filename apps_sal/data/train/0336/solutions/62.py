from collections import defaultdict


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        mapper1 = defaultdict(int)
        mapper2 = defaultdict(int)
        for i in range(len(s)):
            mapper1[s[i]] += 1
            mapper2[t[i]] += 1
        count = 0
        for (char, val) in mapper1.items():
            diff = val - mapper2[char]
            if diff > 0:
                count += diff
        return count
