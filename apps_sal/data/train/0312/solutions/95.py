class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix = [0] * (len(A)+1)
        for i in range(len(A)):
            prefix[i+1] = A[i] + prefix[i]
        
        ans = len(A) + 1
        monoq = deque()
        for i in range(len(prefix)):
            while monoq and prefix[i] <= prefix[monoq[-1]]:
                monoq.pop()
            while monoq and prefix[i] - prefix[monoq[0]]>=K:
                ans = min(ans, i-monoq.popleft())
                
            monoq.append(i)
            
        return ans if ans<len(A)+1 else -1
