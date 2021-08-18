class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for i in range(len(rating) - 2):
            for j in range(i, len(rating) - 1):
                for k in range(j, len(rating)):
                    if rating[i] > rating[j] > rating[k]:
                        result += 1
                    if rating[i] < rating[j] < rating[k]:
                        result += 1
        return result
