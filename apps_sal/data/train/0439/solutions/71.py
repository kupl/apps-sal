class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        #Longest, dp, or memoisation
        
        if(len(A)==0):return 0
        if(len(A)==1):return 1
        max_t=1
        sgn=0 #1: next array should be larger, -1:smaller, 0:new
        current_l=0
        i=0
        while True:      
            #print(A[i],current_l,sgn)
            if(sgn==1 and A[i]>A[i-1]):
                sgn=-sgn
                current_l+=1 
            elif(sgn==-1 and A[i]<A[i-1]):
                sgn=-sgn
                current_l+=1              
            elif(sgn==0):
                current_l=1
                if(i < len(A)-1):
                    if(A[i+1]>A[i]):
                        sgn=1
                    elif(A[i+1]<A[i]):
                        sgn=-1
                    else:
                        sgn=0                
            else:
                i+=-1 #back!
                max_t=max(current_l,max_t)
                current_l=1
                if(i < len(A)-1):
                    if(A[i+1]>A[i]):
                        sgn=1
                    elif(A[i+1]<A[i]):
                        sgn=-1
                    else:
                        sgn=0
                else:
                    #already end
                    max_t = max(max_t,1)   
            i+=1
            if(i==len(A)):
                break
        max_t=max(current_l,max_t) 
        return max_t
        
                    
                    
                
            

