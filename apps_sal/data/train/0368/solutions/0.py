class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        (total, res) = (0, 0)
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res
