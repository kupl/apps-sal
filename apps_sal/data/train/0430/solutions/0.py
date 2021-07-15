class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        seen = dict()
        
        a = 1
        for i in range(n):
            char = s[i]
            b = 2 * a
            if char in seen:
                b -= seen[char]
            
            b %= MOD
            seen[char] = a
            a = b
        return a - 1
                

