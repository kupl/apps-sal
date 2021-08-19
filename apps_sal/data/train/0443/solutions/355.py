class Solution:

    def numTeams(self, rating: List[int]) -> int:
        if len(rating) > 2:
            count = 0
            D = {}
            for i in range(len(rating)):
                for j in range(i + 1, len(rating)):
                    if rating[i] < rating[j]:
                        for k in range(j + 1, len(rating)):
                            if rating[j] < rating[k]:
                                count += 1
                    elif rating[i] > rating[j]:
                        for k in range(j + 1, len(rating)):
                            if rating[j] > rating[k]:
                                count += 1
            return count
        return 0
