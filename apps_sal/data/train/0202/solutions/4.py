class Solution:
    
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        prefix = [1] * N
        suffix = [1] * N
        
        for i, num in enumerate(A[1:], 1):
            i_rev = N - i - 1
            prefix[i] = prefix[i-1] + 1 if A[i-1] < num else 1
            suffix[i_rev] = suffix[i_rev+1] + 1 if A[i_rev] > A[i_rev+1] else 1
            
        ans = 0
        for i, num in enumerate(A):
            left = prefix[i]
            right = suffix[i]
            length = left + right - 1
            
            if length >= 3 and min(left, right) > 1:
                ans = max(ans, length)
        
        return ans

