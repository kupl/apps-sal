class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        q = collections.deque()
        n = len(A)
        B = [0] * (n + 1)
        for i in range(n):
            B[i+1] = A[i] + B[i]
        
        res = float('inf')
        for i in range(n + 1):
            while q and B[i] < B[q[-1]]:   # maintain increasing Manatonic queue
                q.pop()
            
            while q and B[i] - B[q[0]] >= K:   # find the nearest previous element with sum at least K
                res = min(res, i - q.popleft())
            
            q.append(i)
        
        return res if res != float('inf') else -1
