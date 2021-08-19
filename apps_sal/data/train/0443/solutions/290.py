class Solution:

    def numTeams(self, rating: List[int]) -> int:
        sum = 0
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    if rating[i] < rating[j] < rating[k]:
                        sum += 1
                    if rating[len(rating) - 1 - i] < rating[len(rating) - 1 - j] < rating[len(rating) - 1 - k]:
                        sum += 1
        return sum
