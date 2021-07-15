class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        ls = [0 for _ in range(n)]
        rs = [0 for _ in range(n)]
        
        for i in range(n):
            ls[i] = arr[i] + (ls[i-1] if i > 0 else 0)
        for i in range(n-1, -1, -1):
            rs[i] = arr[i] + (rs[i+1] if i < n-1 else 0)
        
        ms = 0
        minls = 0
        for i in range(n):
            minls = min(minls, ls[i])
            ms = max(ms, ls[i]-minls)
        
        mls = max(ls)
        mrs = max(rs)
        ss = sum(arr)
        
        if k == 1:
            return ms
        else:
            if ss < 0:
                return max(ms, mls + mrs) % mod
            else:
                return max(ms, mls + mrs + (k-2) * ss) % mod
        
        
        
        
        
        
        
    
        
        

