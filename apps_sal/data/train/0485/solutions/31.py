from collections import deque

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipped = 0
        q = deque()
        flips = 0
        for i in range(len(A)):
            if len(q) == K:
                flipped ^= q.popleft()
            
            if flipped == A[i]:
                if i + K > len(A):
                    return -1
                flipped ^= 1
                flips += 1
                q.append(1)
            else:
                q.append(0)
        
        return flips

