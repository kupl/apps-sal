class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        N = len(A)
        if N == 1:
            return 0
        A.sort()
        diff = A[-1]-A[0]
        for i in range(N-1):
            maxi = max(A[i]+K, A[N-1]-K)
            mini = min(A[0]+K, A[i+1]-K)
            diff = min(diff, maxi-mini)
        return diff
