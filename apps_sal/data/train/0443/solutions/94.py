class Solution:

    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k] or (rating[i] > rating[j] and rating[j] > rating[k]):
                        ans += 1
        return ans
