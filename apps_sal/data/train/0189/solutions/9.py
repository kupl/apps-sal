import numpy as np

class Solution:    
    
    def check_happy(self,x,y,u,v,fmatrix,unhappy): 
        if(fmatrix[x][u]>fmatrix[x][y] and fmatrix[u][x]>fmatrix[u][v]):
            unhappy.add(x)
            unhappy.add(u)
   
    def unhappyFriends(self, n, preferences, pairs) -> int:
        unhappy = set()
        fmatrix = np.zeros((n,n),dtype=int)
        for i,friendpref in enumerate(preferences):
            for j,pref_ind in enumerate(friendpref):
                fmatrix[i][pref_ind] = n-1-j

        for i in range(n//2-1):
            for j in range(i+1, n//2):
                x,y,u,v = pairs[i][0],pairs[i][1],pairs[j][0],pairs[j][1]
                self.check_happy(x,y,u,v,fmatrix,unhappy)
                self.check_happy(x,y,v,u,fmatrix,unhappy)
                self.check_happy(y,x,u,v,fmatrix,unhappy)
                self.check_happy(y,x,v,u,fmatrix,unhappy)
                
                    
        return len(unhappy)
