from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        c = 0

        c1 = Counter()
        c2 = Counter(s)

        for i in range(len(s)):

            c1[s[i]] += 1
            c2[s[i]] -= 1

            if self.Count(c1) == self.Count(c2):
                c += 1

        return c

    def Count(self, counter):
        return sum([1 for k in counter if counter[k] != 0])
