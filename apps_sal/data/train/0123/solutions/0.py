import math
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        s=0
        c=0
        r=0
        x=math.factorial(N)
        while(True):
            c=x*((N-r-K)**(L-K))*(-1)**(r)//(math.factorial(N-r-K)*math.factorial(r))
            if(c!=0):
                s=(s+c)%(10**9+7)
                r+=1
            else:
                return s

