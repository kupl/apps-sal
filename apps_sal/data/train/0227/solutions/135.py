class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left,right = 0,0
        num_zeros = 0
        window_size = 0
        
        while right < len(A):
            if A[right] == 0:
                num_zeros += 1
            while num_zeros > K:
                if A[left] == 0:
                    num_zeros -= 1
                left += 1 
            window_size = max(window_size,right-left+1)
            right += 1
            
        return window_size    
