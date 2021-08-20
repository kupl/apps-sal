class Solution:

    def numTeams(self, rating: List[int]) -> int:
        count = 0
        l = len(rating)
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if rating[i] < rating[j] < rating[k]:
                        count += 1
                    elif rating[i] > rating[j] > rating[k]:
                        count += 1
        return count
