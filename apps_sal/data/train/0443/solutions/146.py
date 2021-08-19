class Solution:

    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        n = len(rating)
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        ans += 1
        rating.reverse()
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        ans += 1
        return ans
