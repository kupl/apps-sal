class Solution:

    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        count = 0
        for i in range(0, l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        count += 1
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        count += 1
        return count
