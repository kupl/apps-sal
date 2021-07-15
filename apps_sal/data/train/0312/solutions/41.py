class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)  #append the current sum +=x
            
        ans = N + 1 
        monoq = collections.deque()
        for y, Py in enumerate(P):
            while monoq and Py < P[monoq[-1]]:
                monoq.pop()
                
            while monoq and Py - P[monoq[0]] >=K:
                ans = min(ans, y-monoq.popleft())
            monoq.append(y)
        if ans < N+1:
            
            return ans
        else:
            return -1 
        
        
        
        
        # if not A:
        #     return -1 
        # sum = 0 
        # for i in range(len(A)):
        #     sum += A[i] 
        #     if sum < K:
        #         i +=1 
        #     elif sum > K:
        #         i -=1 
        #     else:
        #         return i+1 
        # return -1 

