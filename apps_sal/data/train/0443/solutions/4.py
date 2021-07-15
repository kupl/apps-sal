# x x x x x
#   i   j

# xi != xj

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            firstChoice = rating[i]
            for j in range(i + 1, len(rating)):
                secondChoice = rating[j]
                for k in range(j + 1, len(rating)):
                    thirdChoice = rating[k]
                    if (firstChoice < secondChoice < thirdChoice) or (firstChoice > secondChoice > thirdChoice):
                        count += 1
        return count        
            

