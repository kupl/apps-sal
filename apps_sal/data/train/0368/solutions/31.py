class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        total = res = 0
        s.sort()
        while s and s[-1] + total >= 0:
            total += s.pop()
            res += total
        return res
