class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result=0
        if len(rating)<3:
            result=0
            return result
        
        for i in range(1, len(rating)-1):
            
            # from small to large
            for j in range(0,i):
                if(rating[j]<rating[i]):
                    for k in range(i+1, len(rating)):
                        if rating[i]<rating[k]:
                            result+=1
            
            
            # from large to small
            for j in range(0,i):
                if(rating[j]>rating[i]):
                    for k in range(i+1, len(rating)):
                        if rating[i]>rating[k]:
                            result+=1
        return result
