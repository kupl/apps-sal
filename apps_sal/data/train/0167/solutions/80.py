class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        table = dict()
        def dp(K: int, N: int) -> int:
            if (K == 1) : return N
            if (N <= 0) : return 0
            
            if (K, N) in table: return table[(K, N)];
            lo, hi = 1, N
            res = N
            while (lo <= hi):
                mid = lo + (hi - lo) // 2
                up = dp(K, N - mid)
                dn = dp(K-1, mid-1)
                if (up >= dn): 
                    lo = mid + 1
                    res = min(res, 1 + up)
                else: 
                    hi = mid - 1
                    res = min(res, 1 + dn)
            table[(K, N)] = res
            return res
        return dp(K, N)
        

