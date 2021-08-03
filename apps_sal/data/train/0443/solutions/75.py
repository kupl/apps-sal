class Solution:
    def numTeams(self, rating) -> int:
        n = len(rating)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k]:
                        ans += 1
                    if rating[i] > rating[j] > rating[k]:
                        ans += 1

        return ans
