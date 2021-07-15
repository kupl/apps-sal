class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        
        Fliped = [0]*len(A)
        cnt = 0
        for i in range(len(A)):
            if i >=K:
                fliped = cnt - Fliped[i-K]
            else:
                fliped = cnt
                
            if (A[i] == 0 and fliped % 2 == 0) or (A[i] == 1 and fliped % 2 == 1):
                if i + K > len(A):
                    return -1                
                A[i] = 1
                cnt += 1
                
            Fliped[i] = cnt
            

                    
        return cnt
                    

