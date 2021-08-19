class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for i in range(len(rating) - 2):
            for j in range(i, len(rating) - 1):
                for k in range(j, len(rating)):
                    if (rating[i] > rating[j]) & (rating[j] > rating[k]):
                        cnt += 1
                    elif (rating[i] < rating[j]) & (rating[j] < rating[k]):
                        cnt += 1
                    # print([i, j, k], [rating[i], rating[j], rating[k]], cnt)
        return cnt
