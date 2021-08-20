class Solution:

    def numTeams(self, rating: List[int]) -> int:
        resultCounter = 0
        n = len(rating)
        for i in range(n - 2):
            for j in range(i, n):
                for k in range(j, n):
                    if rating[k] < rating[j] < rating[i] or rating[k] > rating[j] > rating[i]:
                        resultCounter += 1
        return resultCounter
