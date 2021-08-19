class Solution:

    def minSteps(self, s: str, t: str) -> int:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        return int(sum((abs(t.count(l) - s.count(l)) for l in abc)) / 2)
