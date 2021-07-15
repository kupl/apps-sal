class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        if len(A) == 1:
            
            return 1 if A[0] <= K else -1
        
        min_len = len(A) + 1
        
        dq = []
        
        pref = [0]
        
        for i in range(len(A)):
            
            pref.append(pref[- 1] + A[i])
            
        for i in range(len(pref)):
            
            # print(dq)
            
            while dq and pref[i] <= pref[dq[-1]]:
                
                dq.pop(-1)
                
            while dq and pref[i] - pref[dq[0]] >= K:
                
                min_len = min(min_len, i - dq[0])
                
                dq.pop(0)
                
            dq.append(i)
            
        return min_len if min_len < len(A) + 1 else -1
