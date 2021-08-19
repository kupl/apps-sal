class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        n = len(rating)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if rating[i] < rating[j]:
                    for k in range(j + 1, n):
                        if rating[k] > rating[j]:
                            count += 1
                elif rating[i] > rating[j]:
                    for k in range(j + 1, n):
                        if rating[k] < rating[j]:
                            count += 1
        return count
