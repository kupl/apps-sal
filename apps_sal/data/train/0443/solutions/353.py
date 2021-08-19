class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] > rating[j]:
                            count += 1
                elif rating[i] > rating[j]:
                    for k in range(j + 1, len(rating)):
                        if rating[k] < rating[j]:
                            count += 1
        return count
