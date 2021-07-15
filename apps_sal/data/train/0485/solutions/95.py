class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipped = 0
        status = [0] * len(A)
        flips = 0
        for i in range(len(A)):
            if i >= K:
                flipped ^= status[i - K]
            
            if flipped == A[i]:
                if i + K > len(A):
                    return -1
                flipped ^= 1
                flips += 1
                status[i] = 1
        
        return flips

