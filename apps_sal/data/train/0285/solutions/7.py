class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        mini = A[0]
        maks = A[-1]
        res = maks - mini
        for i in range(len(A)-1):
            res = min(res, max(maks-K, A[i]+K) - min(mini+K, A[i+1]-K))   
        return res

