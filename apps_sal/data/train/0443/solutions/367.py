class Solution:
    def numTeams(self, rating: List[int]) -> int:

        output = 0

        for k in range(len(rating) - 2):
            for j in range(k + 1, len(rating) - 1):
                if (rating[j] > rating[k]):
                    for i in range(j + 1, len(rating)):
                        if (rating[i] > rating[j]):
                            output += 1
                if (rating[j] < rating[k]):
                    for i in range(j + 1, len(rating)):
                        if (rating[i] < rating[j]):
                            output += 1

        return output
