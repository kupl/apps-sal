class Solution:
    
    def rabinKarp(self, L, nums):
        h = 0
        a = 26
        MOD = 2**32
        for i in range(L):
            h = (h * a + nums[i]) % MOD
           
        aL = pow(a, L, MOD)
        seen = {h}
        for start in range(1, len(nums)-L+1):
            h = (h *a - nums[start-1] * aL + nums[start+L-1]) % MOD
            if h in seen:
                return start
            seen.add(h)
        return -1
    
    def longestDupSubstring(self, S: str) -> str:   
        nums = [ord(ch)-ord('a') for ch in S]
        l, r = 0, len(S)
        while l < r:
            mid = l + (r-l) // 2
            if self.rabinKarp(mid, nums) != -1:
                l = mid + 1
            else:
                r = mid
        start = self.rabinKarp(l-1, nums)
        return S[start:start+l-1]        
            

