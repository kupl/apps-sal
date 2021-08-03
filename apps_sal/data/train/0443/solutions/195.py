class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        N = len(rating)
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    ans += int(rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k])

        return ans
