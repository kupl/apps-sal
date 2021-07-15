class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        n = len(arr)
        mod_count = [0 for i in range(0,k)]
        
        
        for i in range(0,n):
            mod_count[arr[i]%k]+=1
            
            
        #print(mod_count)
        
        mid = int(k/2)
        #print(\"mid = %d\" %mid)
        
        if(k%2==1):     #odd bucket [0], [1,k-1], [2,k-1], ...[mid-1,mid+1]
            if(mod_count[0]%2==1):
                #print(\"debug0\")
                return False
        else:           #even bucket [0], [1,k-1], [2,k-2], ...[mid]
            if(mod_count[0]%2==1 or mod_count[mid]%2==1):
                #print(\"debug1\")
                return False

        num = int((k-1)/2)
        
        for i in range(1,num+1):
            #print(i,k-1-i)
            if(mod_count[i]!=mod_count[k-i]):
                #print(\"debug2\")
                return False
        
        return True
