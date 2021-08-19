class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    direction = 1
                else:
                    direction = 0
                for k in range(j + 1, n):
                    if direction and rating[k] > rating[j]:
                        ans += 1
                    if not direction and rating[k] < rating[j]:
                        ans += 1
        return ans
