class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        r = 0
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if rating[i] < rating[j] < rating[k]:
                        r += 1
                    if rating[i] > rating[j] > rating[k]:
                        r += 1
        return r
