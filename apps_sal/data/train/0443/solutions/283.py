class Solution:

    def numTeams(self, rating: List[int]) -> int:
        nTeams = 0
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    if rating[j] > rating[i]:
                        if rating[k] > rating[j]:
                            nTeams += 1
                    elif rating[j] < rating[i]:
                        if rating[k] < rating[j]:
                            nTeams += 1
        return nTeams
