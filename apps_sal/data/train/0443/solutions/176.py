class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                k = j+1
                while(k<len(rating)):
                    if (rating[k]>rating[j]) and (rating[j]>rating[i]):
                        count = count+1
                    elif(rating[k]<rating[j]) and (rating[j]<rating[i]):
                        count = count+1
                    k = k+1
            
        return count

