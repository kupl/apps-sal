class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        result = 0
        left, right, count = 0, 0, 0
        for right in range(len(A)):
            S -= A[right]
            if A[right] == 1:
                count = 0
            while S <= 0 and left <= right:
                if S == 0:
                    count += 1
                S += A[left]
                left += 1
            result += count
        return result
            
                
                    
            
            

