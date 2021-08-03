class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1, cnt2 = list(map(collections.Counter, (s, t)))

        return sum((cnt1 - cnt2).values())
