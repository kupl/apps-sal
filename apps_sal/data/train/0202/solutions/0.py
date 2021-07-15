class Solution:
    def longestMountain(self, A: List[int]) -> int:
        up=0
        down=0
        ans=0
        for i in range(0,len(A)-1):
            if A[i]<A[i+1]:
                if down==0:
                    up+=1
                else:
                    up=1
                    down=0
                    
            elif A[i]>A[i+1]:
                if up>0:
                    down+=1
                    mountain=up+down+1
                    if ans<mountain:
                        ans=mountain
                
            else:
                up=0
                down=0

            
        
        return ans
