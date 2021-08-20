class Solution:

    def numTeams(self, rating: List[int]) -> int:
        c = 0
        (i, j, k) = (0, 0, 0)
        n = len(rating)
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] > rating[j]:
                        break
                    if rating[i] < rating[j] < rating[k]:
                        c += 1
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if rating[i] < rating[j]:
                        break
                    if rating[i] > rating[j] > rating[k]:
                        c += 1
        return c
