class Solution:
    def minKBitFlips(self, A: List[int], k: int) -> int:
        n = len(A)
        count = [0] * n
        ps = 0
        res = 0
        
        for i in range(n-k+1):
            flip = ps + A[i]
            if flip % 2 == 0:
                count[i] = 1
                res += 1
                ps += 1
            
            if i - k + 1 >= 0:
                ps -= count[i-k+1]
        
        
        for i in range(n-k+1, n):
            if (ps + A[i]) % 2 == 0:
                return -1
            ps -= count[i-k+1]
        
        return res
