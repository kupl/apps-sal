class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        length = len(rating)
        for i in range(length - 2):
            for j in range(i, length - 1):
                for k in range(j, length):
                    if rating[i] > rating[j] > rating[k]:
                        cnt += 1
                    if rating[i] < rating[j] < rating[k]:
                        cnt += 1
        return cnt
