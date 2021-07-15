class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0;
        for i in range(0,len(rating)):
            for j in range(1,len(rating)):
                for k in range(2,len(rating)):
                    if (j>i and k>j) and ((rating[i]<rating[j] and rating[j]<rating[k]) or (rating[i]>rating[j] and rating[i]>rating[k] and rating[j]>rating[k])):
                        count=count+1
        return count
