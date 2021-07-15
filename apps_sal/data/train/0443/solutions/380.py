class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        for i in range(0,len(rating)-2):
            for j in range(i+1,len(rating)):
                flag=0
                if rating[j]>rating[i]:
                    flag=1
                else:
                    flag=0
                for k in range(j+1,len(rating)):
                    if flag==1:
                        if rating[k]>rating[j]:
                            count=count+1
                    else:
                        if rating[k]<rating[j]:
                            count=count+1
        return count
                        
                    

