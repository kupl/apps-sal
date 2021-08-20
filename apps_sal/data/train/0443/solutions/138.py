class Solution:

    def numTeams(self, rating: List[int]) -> int:
        i = 0
        j = 0
        k = 0
        numOfTeams = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        numOfTeams += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        numOfTeams += 1
        return numOfTeams
