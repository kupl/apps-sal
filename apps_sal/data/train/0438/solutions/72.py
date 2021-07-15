class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) ==m:
            return m
        n = len(arr)
        max_length = [0]*(n+2)
        result = -1
        for step, i in enumerate(arr):
            left, right = max_length[i-1],  max_length[i+1]
            if left == m or right == m:
                result = step 
            
            max_length[i-left] = max_length[i+right] = left + right + 1
        
        return result
                

