class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        v_min, v_max = A[0], A[-1]
        res = v_max - v_min
        for i in range(len(A)-1):
            res = min(res, max(v_max-K, A[i]+K) - min(v_min+K, A[i+1]-K))
        return res
