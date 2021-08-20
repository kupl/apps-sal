class Solution:

    def numTeams(self, ratings: List[int]) -> int:
        n = len(ratings)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if ratings[i] < ratings[j] < ratings[k]:
                        count += 1
                    if ratings[i] > ratings[j] > ratings[k]:
                        count += 1
        return count
