class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n=len(rating)
        
        if n<3:
            return 0
        
        teams=0
        for x in range(n):
            for y in range(x+1,n):
                for z in range(y+1,n):
                    a,b,c=rating[x],rating[y],rating[z]
                    if (a>b>c) or (a<b<c):
                        teams+=1
        
        return teams

