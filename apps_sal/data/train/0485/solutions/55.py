class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        i=0
        c=0
        q=collections.deque()
        sign=0
        
        for i in range(len(A)):
            
            if q and i==q[0]:
                sign=1-sign
                q.popleft()
            
            if A[i]!=sign:
                continue
            else:
                if i+K>len(A):
                    return -1
                
                q.append(i+K)
                sign=1-sign
                c+=1
                
        return c
    
    
            
            
                

