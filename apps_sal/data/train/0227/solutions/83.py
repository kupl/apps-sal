class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        max_length = 0
        start = 0
        end = 1 
        
        zeros = 0
            
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        
        zeros = 2 - sum(A[:2])
        
        while end < len(A):
                           
            valid = zeros <= K
            
            if valid:
                max_length = max(max_length, (end - start)+1)
                end += 1
                if end == len(A):
                    return max_length
                
                if A[end] == 0:
                    zeros += 1
            else:
                if A[start] == 0:
                    zeros -= 1
                start += 1
        return max_length

