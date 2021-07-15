class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        
        n = len(A)
        ff = [0 for i in range(n)]
        
        
        
        cur = 0
        f = 0
        for i in range(n):
            
            cur += ff[i]
            xo = cur % 2
            if xo ^ A[i] == 0:
                if i + K - 1 > n - 1:
                    return -1
                else:
                    f += 1
                    ff[i] += 1
                    if i + K < n:
                        ff[i + K] -= 1
                    cur += 1
        return f
