class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ratingLen = len(rating)
        result = 0
        for i in range(ratingLen - 2):
            for j in range(i + 1, ratingLen - 1):
                for k in range(j + 1, ratingLen):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        result += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        result += 1
        return result
