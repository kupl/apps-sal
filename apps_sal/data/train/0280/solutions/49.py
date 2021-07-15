class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        def substring_palindrome(substring):
            l = 0
            r = len(substring) - 1
            ans = 0
            while l <= r:
                if substring[l] != substring[r]:
                    ans += 1
                l += 1
                r -= 1
            
            return ans
        
    
        n = len(s)  
        dp = {}
                    
        
        def backtrack(i, cuts):
            if (i, cuts) not in dp:
                # K is not cuts but subdivisions
                if cuts == 1:
                    dp[(i, cuts)] = substring_palindrome(s[:i+1])
                else:
                    ans = float('inf')
                    for end in range(cuts-2, i):
                        ans = min(ans, substring_palindrome(s[end+1:i+1]) + backtrack(end, cuts-1))
                    dp[(i, cuts)] = ans
                
                
                
            return dp[(i, cuts)]
        
        return backtrack(n-1, k)
