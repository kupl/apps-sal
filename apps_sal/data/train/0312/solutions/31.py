class Solution:
    def shortestSubarray(self, arr, k):
        n = len(arr)
        
        # build prefix sums
        pSums = [0]
        for x in arr:
            pSums.append(pSums[-1] + x)
            
        res = n + 1
        q = deque()
        
        for y, Py in enumerate(pSums):
            while q and Py <= pSums[q[-1]]:
                q.pop()
                
            while q and Py - pSums[q[0]] >= k:
                res = min(res, y - q.popleft())

            q.append(y)
            
        return res if res < n + 1 else -1
        
            

