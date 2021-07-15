class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count = maxS = j = 0
        
        for i, a in enumerate(A):
            if a == 0:
                count += 1
            
            while j < len(A) and count > K:
                if A[j] == 0:
                    count -= 1
                j += 1
                
            maxS = max(maxS, i-j+1)
            
        return maxS
