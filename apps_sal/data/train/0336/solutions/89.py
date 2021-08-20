from collections import Counter


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count = 0
        for char in t:
            if count_s[char] > 0:
                count_s[char] -= 1
            else:
                count += 1
        return count
