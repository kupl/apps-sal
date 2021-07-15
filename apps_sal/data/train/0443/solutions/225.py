class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating); numberOfTeams = 0
        for i in range(0, length):
            for j in range(0, length):
                if i < j:
                    for k in range(0, length):
                        if j < k:
                            if rating[i] < rating[j] and rating[j] < rating[k]:
                                numberOfTeams = numberOfTeams + 1
                            elif rating[i] > rating[j] and rating[j] > rating[k]:
                                numberOfTeams = numberOfTeams + 1
        return numberOfTeams
