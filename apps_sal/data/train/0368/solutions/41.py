class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sortlist = sorted(satisfaction, reverse=True)
        a = 0
        b = 0
        for i in range(len(sortlist)):
            a += sortlist[i]
            if a <= 0:
                break
            else:
                b += 1
        return sum(sortlist[j] * (b - j) for j in range(0, b))
