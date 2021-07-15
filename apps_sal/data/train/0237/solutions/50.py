class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        i, s, res, count = 0, 0, 0, 1
        
        for j in range(len(A)): 
            s += A[j]
            while i < j and (s > S or A[i] == 0):
                if A[i]:
                    s -= A[i]
                    count = 1
                else:
                    count += 1 
                i += 1          
                
            if s == S:
                res += count
                
        return res

