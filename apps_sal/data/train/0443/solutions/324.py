class Solution:

    def numTeams(self, rating: List[int]) -> int:
        output = 0
        for i in range(len(rating)):
            for j in range(len(rating)):
                if i >= j:
                    continue
                for k in range(len(rating)):
                    if j >= k:
                        continue
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        output += 1
        return output
