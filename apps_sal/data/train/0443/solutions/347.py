class Solution:

    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating) - 1):
                if rating[i] < rating[j]:
                    for k in range(j, len(rating)):
                        if rating[j] < rating[k]:
                            res += 1
                else:
                    for k in range(j, len(rating)):
                        if rating[j] > rating[k]:
                            res += 1
        return res
