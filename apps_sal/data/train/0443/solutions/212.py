class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res=0
        for i in range(0,len(rating)):
            for j in range(i+1,len(rating)):
                for k in range(j+1,len(rating)):
                    if ((rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])):
                        res+=1
        return res
