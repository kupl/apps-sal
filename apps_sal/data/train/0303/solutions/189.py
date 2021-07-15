class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        maxSoFar = [0]*N
        for i in range(N):
            curMax = 0
            for prev in range(1,min(i+1,k)+1):
                curMax = max(curMax,arr[i-prev+1])
                lastPartition = maxSoFar[i-prev] if i >= prev else 0
                maxSoFar[i] = max(maxSoFar[i], lastPartition + curMax*prev)
        return maxSoFar[-1]
