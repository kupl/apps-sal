from collections import deque
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        reduceInds = deque()
        if K == 1:
            return len(A) - sum(A)
        
        maxFlipCnt = 0
        effectiveFlipCnt = 0
        for i,b in enumerate(A):
            if len(reduceInds) != 0 and reduceInds[0] == i:
                effectiveFlipCnt -= 1
                reduceInds.popleft()
            
            if b == 0 and effectiveFlipCnt % 2 == 0 or b == 1 and effectiveFlipCnt % 2 == 1:
                if i >= len(A) - K + 1: # No way to flip now, just check if it is 0
                    return -1
                else:
                    maxFlipCnt+=1
                    effectiveFlipCnt+=1
                    reduceInds.append(i + K)
        
        return maxFlipCnt
        
                
        

