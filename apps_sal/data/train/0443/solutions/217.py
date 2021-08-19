class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if (rating[k] < rating[j]) & (rating[j] < rating[i]):
                        count += 1
                    elif (rating[k] > rating[j]) & (rating[j] > rating[i]):
                        count += 1
        return count
