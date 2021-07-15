class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        P = [0]
        for _ in range(2):
            for v in A:
                P.append(P[-1] + v)
        
        ans = A[0]
        q = collections.deque([0])
        for j in range(1, len(P)):
            while q and  j - q[0]  > N:
                q.popleft()
            
            ans = max(ans, P[j] - P[q[0]])
            
            while q and P[q[-1]] >= P[j]:
                q.pop()
            q.append(j)     
            
        return ans

