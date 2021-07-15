class Solution:
    def numTeams(self, rating: List[int]) -> int:
        z=len(rating)
        final=[]
        if z<3 :
            return 0
        for i in range (0,z):
            for j in range (i+1,z):
                for k in range (j+1,z):
                    if  (rating[i]<rating[j] and rating[j]<rating[k]) or (rating[i]>rating[j] and rating[j]>rating[k]) :
                        final.append((i,j,k))
                        
        final=set(final)
        return len(final)
                        
            
                        

