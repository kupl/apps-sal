class Solution:

    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        ans += 1
        return ans
