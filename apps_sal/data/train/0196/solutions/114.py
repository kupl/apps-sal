class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        B = A + A
        pfx = [0]
        for x in B:
            pfx.append(pfx[-1] + x)
        dq = collections.deque()
        ans = A[0]
        dq.append(0)
        #monoqueue dq that contains indices i such that P[i]s are non-decreasing
        for j in range(1,len(pfx)):
            if j - dq[0] > n:
                dq.popleft()
            
            ans = max(ans, pfx[j] - pfx[dq[0]])
            
            while dq and pfx[dq[-1]] > pfx[j]:
                dq.pop()
            
            dq.append(j)
        return ans
