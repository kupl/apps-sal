class Solution:

    def numTeams(self, rating):
        length = len(rating)
        num_combinations = 0
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if rating[i] < rating[j]:
                        if rating[j] < rating[k]:
                            num_combinations = num_combinations + 1
                    elif rating[i] > rating[j]:
                        if rating[j] > rating[k]:
                            num_combinations = num_combinations + 1
        return num_combinations
