from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        for i in set(s):
            if(s.count(i) > t.count(i)):
                count += s.count(i) - t.count(i)
        return count
