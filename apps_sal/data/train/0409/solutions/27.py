class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        current = arr[0]
        glob    = arr[0]
        
        for i in range(1, len(arr)):
            
            if current + arr[i] >= arr[i]:
                current += arr[i]
            else:
                current = arr[i]
                
            if current > glob:
                glob = current
                
        print((current, glob))
        if k==1:
            return glob if glob > 0 else 0
        
        prevCurrent = current
        prevGlob    = glob
        
        for i in range(len(arr)):
            
            if current + arr[i] >= arr[i]:
                current += arr[i]
            else:
                current = arr[i]
                
            if current > glob:
                glob = current
        
        if prevGlob == glob or k==2:
            return glob if glob > 0 else 0
        
        afterCurrent = current
        afterGlob    = glob
        
        for i in range(len(arr)):
            
            if current + arr[i] >= arr[i]:
                current += arr[i]
            else:
                current = arr[i]
                
            if current > glob:
                glob = current
                
                
        glob += (glob - afterGlob) * (k-3)
        
        return glob % 1000000007 if glob > 0 else 0
            
            

