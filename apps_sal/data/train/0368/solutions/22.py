class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        s = sorted(satisfaction, reverse=True)
        total = 0
        i = 0
        while i < len(satisfaction):
            total = max(sum([x * (i + 1) for i, x in enumerate(s[0:i + 1][::-1])]), total)
            i += 1
        return total
