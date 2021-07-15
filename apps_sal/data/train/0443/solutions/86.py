class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        c = 0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        c += 1
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        c += 1     
        return c

