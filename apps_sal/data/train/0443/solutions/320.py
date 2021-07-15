class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = []
        for i in range(len(rating)):
            for j in range(len(rating)):
                for k in range(len(rating)):
                    if i<j<k and (rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]):
                        result.append(rating)
        return len(result)

