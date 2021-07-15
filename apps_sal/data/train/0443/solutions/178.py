class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        else:
            res = 0
            for i in range(len(rating)-2):
                for j in range(i, len(rating)-1):
                    for k in range(j, len(rating)):
                        if(rating[i]>rating[j] and rating[j]>rating[k]):
                            res += 1
                        elif(rating[i]<rating[j] and rating[j]<rating[k]):
                            res += 1
            return res
                            
                

