class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        l = 0
        r = len(S)
        base = 26
        mod = 2**32
        res = [0, 0]
        nums = [ord(n) - ord('a') for n in S]

        
        while l < r:
            
            mid = (l+r) // 2
            h = 0
            
            for i in range(0, mid):
                h = (h*base + nums[i]) % mod
                
            dups = set([h])
            remove = pow(base, mid, mod)
            
            for i in range(1, len(nums) - mid + 1):
                h = (h*base - nums[i-1] * remove + nums[i+mid-1]) % mod
                
                if h in dups:
                    res = [i, i+mid]
                    break
                    
                dups.add(h)
                # print(mid, h)         
            if res[1] - res[0] < mid:
                r = mid
            else:
                l = mid + 1
            
                
        return S[res[0]:res[1]]
                
                

