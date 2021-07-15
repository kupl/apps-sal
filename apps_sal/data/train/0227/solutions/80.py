class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        left = 0
        right = 0 
        
        k = K
        max_ans = 0
        so_far = 0
        while(right < len(A)):
            if(A[right]==1):
                right+=1
            else:
                if(k>0):
                    right+=1
                    k-=1
                else:
                    if(A[left]==0):
                        k+=1
                    left+=1
            
            max_ans = max(max_ans, right-left)
        
        return max_ans
