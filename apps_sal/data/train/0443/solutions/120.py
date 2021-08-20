class Solution:

    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        cnt += 1
                    elif rating[i] < rating[j] and rating[j] < rating[k]:
                        cnt += 1
        return cnt
