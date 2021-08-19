class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        less_r = [0] * n
        bigger_r = [0] * n
        less_l = [0] * n
        bigger_l = [0] * n
        for i in range(n):
            for j in range(i):
                less_l[i] += rating[i] > rating[j]
                bigger_l[i] += rating[i] < rating[j]
            for j in range(i + 1, n):
                less_r[i] += rating[i] > rating[j]
                bigger_r[i] += rating[i] < rating[j]
        ans = 0
        for i in range(n):
            ans += less_l[i] * bigger_r[i] + less_r[i] * bigger_l[i]
        return ans
