from queue import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        sums=[0]
        for i in A:
            sums.append(sums[-1]+i)
        
        min_l=len(A)+1
        q=deque([])
        
        for i in range(len(sums)):
            while q and sums[q[-1]]>=sums[i]:
                q.pop()
            while q and sums[i]-sums[q[0]]>=K:
                min_l=min(min_l,i-q.popleft())
                
            q.append(i)
        
        if min_l>len(A): return -1
        else: return min_l

