class Solution:

    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if rating[j] > rating[i] and rating[k] > rating[j]:
                        res += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        res += 1
        return res
