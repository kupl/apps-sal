class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        if not arr:
            return 0
        
        if k==1:
            return sum(arr)
        
        self.memo={}
        
        def makepart(arr,n):
            
            if n in self.memo:
                return self.memo[n]
            
            if not arr:
                return 0
            
            l=min(k,len(arr))
            maxele=0
            total=0
            
            for i in range(l):
                
                maxele=max(maxele,arr[i])
                
                temp=(maxele*(i+1))+makepart(arr[i+1:],n+i+1)
                
                total=max(total,temp)
                
            self.memo[n]=total
            
            return total
        
        return makepart(arr,0)
                
            

