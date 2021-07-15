class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        now, m, ans = 0, 0, 0
            
        for i in range(n):
            now += arr[i]
            m = min(m, now)
            ans = max(ans, now-m)
        
        if k==1:
            return ans%(10**9+7)
        
        now, pref_M = 0, 0
        
        for i in range(n):
            now += arr[i]
            pref_M = max(pref_M, now)
        
        now, suf_M = 0, 0
        
        for i in range(n-1, -1, -1):
            now += arr[i]
            suf_M = max(suf_M, now)
        
        ans = max(ans, pref_M+suf_M+max(0, sum(arr))*(k-2))
        return ans%(10**9+7)

