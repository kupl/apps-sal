class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cpt = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] > rating[j]:
                            cpt += 1
                else:
                    for k in range(j + 1, len(rating)):
                        if rating[k] < rating[j]:
                            cpt += 1
        return cpt
