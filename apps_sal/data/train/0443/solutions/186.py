class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        ratings = rating
        for i in range(len(ratings)):
            for j in range(i + 1, len(ratings)):
                for k in range(j + 1, len(ratings)):
                    if ratings[i] > ratings[j] > ratings[k]:
                        count += 1
                    elif ratings[i] < ratings[j] < ratings[k]:
                        count += 1
        
        return count
