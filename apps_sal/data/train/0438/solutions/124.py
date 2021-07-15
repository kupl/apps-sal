class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        lenArr = [0] * (len(arr) + 2)        
        
        count = 0
        steps = 1
        res = -1
        for k in arr:            
            left, right = lenArr[k-1], lenArr[k+1]
            if lenArr[k-left] == m:
                count -= 1 
                
            if lenArr[k+right] == m:
                count -= 1 
                
            lenArr[k] = lenArr[k-left] = lenArr[k+right] = left + right + 1
            if lenArr[k] == m:                
                count += 1
                
            if count > 0:
                res = steps
            
            steps += 1
            
        return res
