class Solution(object):
    def shortestSubarray(self, A, K):
        n = len(A)
        d = collections.deque([(A[0],0)])
        res = n+1
        
        for i in range(1, n):
            A[i] += A[i-1]
        A = [0] + A
        for i in range(n+1):
            while d and d[-1][0] > A[i]: d.pop()
            d.append((A[i], i))
            while d and A[i] - d[0][0] >= K:
                res = min(res, i-d[0][1])
                d.popleft()
            
        return res if res <= n else -1
                
        

