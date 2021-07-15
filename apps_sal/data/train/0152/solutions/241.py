class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        ## need to find the maximum minmum distance 
        ## feasibility is a function of distance
        ## need to find the last feasible solution 
        ## that is the last T 
        
        def check (dist: int) -> bool:
            
            curr = position[0]
            count = 1 
            
            for i in range (len(position)):
                
                #print(abs(position[i]-curr))
                
                if (abs(position[i]-curr)>= dist):
                    
                    curr = position[i]
                    count +=1 
                
                if(i == (len(position)-1)):
                    
                    if (count >= m):
                        return True 
                    else:
                        return False 
                    
        
        ## BS for optimal length 
        
        lo = 1
        hi = (max(position)- min(position))
        
        while (lo<hi):
            
            mid= lo + ((hi-lo+1)//2)
            #print(mid)
            
            if(check(mid)):
                
                lo = mid 
            
            else : 
                hi = mid -1 
                
        
        return (lo)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

