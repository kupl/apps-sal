class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        ans = 0
        for i in range(l):
            for j in range(i, l):
                for k in range(j, l):
                    if rating[i] < rating[j] < rating[k]:
                        ans += 1
                    if rating[i] > rating[j] > rating[k]:
                        ans += 1
        return ans
