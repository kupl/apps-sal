class Solution:
    def numWays(self, s: str) -> int:        
        k = s.count('1')
        if k % 3 != 0: return 0
        n, M = len(s), 10**9 + 7
        if k == 0: return (n-1)*(n-2)//2 % M
        ans, cnt, i = 1, 0, 0         
        while i < len(s):            
            cnt += s[i] == '1'
            if cnt in [k//3, 2*k//3]:
                j = i+1
                while j < len(s) and s[j] == '0': j += 1
                ans *= j-i
                i = j            
            else: i += 1
            if cnt == 2*k//3: break
        return ans % M
                
                

