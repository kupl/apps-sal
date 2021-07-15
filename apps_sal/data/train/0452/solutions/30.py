class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        
        
        
        # my solution ... 1272 ms ... 48 % ... 14.8 MB ... 39 %
        #  time: O(2^n)
        # space: O(n*d)
        
        seen = {}
        def func(sidx, d):  # 返回在 d 天内完成 A[sidx:] 的结果
            if sidx == n or d == 0:
                return 0 if (sidx == n and d == 0) else float('inf')
            if n-sidx < d:
                return float('inf')
            if n-sidx == d:
                return endsum[sidx]
            
            if (sidx, d) not in seen:
                res = float('inf')
                curmax = A[sidx]
                for eidx in range(sidx, n):
                    if curmax < A[eidx]:
                        curmax = A[eidx]
                    res = min(res, curmax + func(eidx+1, d-1))
                seen[sidx, d] = res
            return seen[sidx, d]
        
        n = len(A)
        if n  < d: return -1
        if n == d: return sum(A)
        endsum = [A[-1]] * n
        for j in range(n-2, -1, -1):
            endsum[j] = A[j] + endsum[j+1]
        return func(0, d)
        
        

