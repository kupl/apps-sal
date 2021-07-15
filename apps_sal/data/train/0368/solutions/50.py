class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        max_satisfaction = 0
        satis = 0
        sum_ = 0
        for s in satisfaction:
            satis += sum_ + s
            sum_ += s
            max_satisfaction = max(max_satisfaction, satis)
            if sum_ < 0:
                break
                
        return max_satisfaction

