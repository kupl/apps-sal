class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = total = 0
        i=len(satisfaction)-1
        satisfaction.sort()
        while i>=0 and satisfaction[i]+total > 0:
            total += satisfaction[i]
            res += total
            i-=1
        return res

