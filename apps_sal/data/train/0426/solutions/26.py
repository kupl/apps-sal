import math

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        if(N==1):
            return True
        
        nn=int(math.log(N)/math.log(2))-1
        tmp=2**(nn)
        
        fun=lambda x: sorted( list(str(x)) ,key=lambda x:int(x),reverse=True)
        N=fun(N)
        
        if(N==fun(tmp)):
            return True
        
    #    print(nn,tmp)
        for x in range(nn,20*nn):
            tmp=tmp*2
            if(N==fun(tmp)):
                return True
            if(nn<len(str(tmp))):
                break
        
        tmp=2**(nn)

        for x in range(nn,nn//20,-1):
            tmp=tmp//2
            if(N==fun(tmp)):
                return True
            if(nn<len(str(tmp))):
                break
        return False
        
        
        
            
        
        
        
        
        
            
        
        
        
        

