class Solution:
    def minOperationsMaxProfit(self, cust: List[int], boardingC: int, runningC: int) -> int:
        maxp=curr=rem=ans=rot=0
        i=0
        
        l=len(cust)
        while i<l or rem:
            rot+=1
            rem+=cust[i] if i<l else 0 
            
            if rem>=4:
                curr+=4
                rem-=4
                
            else:
                curr+=rem
                rem=0
                
            
                
            prof=(curr*boardingC)-(runningC*rot)

            if prof>maxp:
                maxp=prof
                ans=rot
                    
            i+=1
                    
        return ans if maxp>0 else -1
                

