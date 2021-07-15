class Solution:
    def numberOfArrays(self, S: str, K: int) -> int:
        import sys
        sys.setrecursionlimit(10**9+7)
        
        @lru_cache(None)
        def ways(idx):
            if idx == len(S): return 1
            if S[idx] == '0': return 0
            
            ans = 0
            num = 0
            for i in range(idx, len(S)):
                num = num*10 + (ord(S[i]) - ord('0'))
                if num > K: break
                
                ans = (ans + ways(i+1)) % 1000000007
            return ans
    
        return ways(0)

