class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        A[0] = A[0]%K
        seen = {0:1}
        count = 0 
        for i in range(1,n):
            A[i] = (A[i] + A[i-1])%K
        for i in range(n):
            newTarget = (A[i] - K)%K
            if newTarget in seen: 
                count+= seen[newTarget]
            if A[i] in seen:
                seen[A[i]] += 1
            else:
                seen[A[i]] = 1
        return count 
            
            
            
        

