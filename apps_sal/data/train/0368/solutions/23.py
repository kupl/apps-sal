class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        dishes = len(satisfaction)
        best = 0
        for i in range(dishes):
            sum = 0
            tmp = satisfaction[-i-1:dishes]
            for j,val in enumerate(tmp):
                sum+=(j+1)*val
            best = max(best,sum)
        return best
