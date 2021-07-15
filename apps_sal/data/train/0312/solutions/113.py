class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefixSum = [0]*(len(A)+1)
        for i in range(1,len(prefixSum)):
            prefixSum[i] = prefixSum[i-1]+A[i-1]
        
        dq = deque()
        shortestLen = sys.maxsize
        
        for i in range(len(prefixSum)):
            while dq and prefixSum[dq[-1]] >= prefixSum[i]:
                dq.pop()
            
            while dq and prefixSum[i]-prefixSum[dq[0]] >= K:
                shortestLen = min(shortestLen,i-dq[0])
                dq.popleft()
            
            dq.append(i)
        return shortestLen if shortestLen != sys.maxsize else -1

