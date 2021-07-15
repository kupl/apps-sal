class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            less_left = 0
            less_right = 0
            greater_left = 0
            greater_right = 0
            
            for j in range(len(rating)):
                if j < i:
                    if rating[i] > rating[j]:
                        less_left += 1
                    elif rating[i] < rating[j]:
                        greater_left += 1
                elif j > i:
                    if rating[i] > rating[j]:
                        less_right += 1
                    elif rating[i] < rating[j]:
                        greater_right += 1
            count += less_left * greater_right + greater_left * less_right
        return count

