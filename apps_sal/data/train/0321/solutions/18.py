class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        arr1=list(s1)
        arr2=list(s2)
        arr1.sort()
        arr2.sort()
        n=len(arr1)
        flag=True

    
        flag1=True
        for i in range(n):
            if arr1[i]<arr2[i]:
                flag1=False
                
        flag2=True
        for i in range(n):
            if arr1[i]>arr2[i]:
                flag2=False
                
    
                
        if flag1 or flag2:
            return True

                
        return False
                
                
                    
                
                
            
        
        
        

