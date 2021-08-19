class Solution:

    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for i in range(len(rating)):
            for j in range(len(rating)):
                if 0 <= i < j:
                    for k in range(len(rating)):
                        if j < k < len(rating):
                            if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                                result += 1
        return result
