class Solution(object):  
     def hIndex(self, citations):  
         """ 
         :type citations: List[int] 
         :rtype: int 
         """  
           
         n=len(citations)  
           
         if n>0:           
             citations.sort()  
             citations.reverse()            
             h=0 
             
             while h<n and citations[h]-1>=h:  
                 h+=1                
             return h  
         else:  
             return 0  
