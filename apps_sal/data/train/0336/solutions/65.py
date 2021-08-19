import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter = collections.Counter(s)

        for c in t:
            # if c in counter:
            counter[c] -= 1

        return sum([abs(x) for x in list(counter.values())]) // 2
