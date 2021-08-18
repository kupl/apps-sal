class Solution:
    def minSteps(self, s: str, t: str) -> int:

        counter = {}
        count = 0

        for c in s:
            counter[c] = counter.get(c, 0) + 1

        for c in t:
            if c in counter and counter[c] > 0:
                counter[c] -= 1
            else:
                count += 1

        return count
