class Solution:

    def numTeams(self, rating: List[int]) -> int:
        pairs = []
        if len(rating) == 1 or len(rating) == 2:
            return 0
        else:
            for i in range(len(rating)):
                for j in range(i + 1, len(rating)):
                    for k in range(j + 1, len(rating)):
                        if rating[i] > rating[j] > rating[k]:
                            pairs.append([rating[i], rating[j], rating[k]])
                        elif rating[i] < rating[j] < rating[k]:
                            pairs.append([rating[i], rating[j], rating[k]])
            return len(pairs)
