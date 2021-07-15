import collections

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        
        if len(A) == 1:
            if A[0] >= K:
                return 1
            return -1
        
        increasing_A = [0]
        for i in A:
            increasing_A.append(increasing_A[-1]+i)
            
        min_length = float('inf')
        queue = collections.deque()
        
        for i,v in enumerate(increasing_A):
            while queue and v <= increasing_A[queue[-1]]:
                queue.pop()
                
            while queue and v-increasing_A[queue[0]] >= K:
                min_length = min(min_length, i-queue.popleft())
            
            queue.append(i)
            
        if min_length == float('inf'):
            return -1
        return min_length
