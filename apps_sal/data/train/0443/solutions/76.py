class Solution:
    def numTeams(self, rating: List[int]) -> int:
        output = 0
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                for k in range(j+1,len(rating)):
                    if rating[i] > rating[j] > rating[k]:
                        output += 1
                    if rating[i] < rating[j] < rating[k]:
                        output += 1
        return output
