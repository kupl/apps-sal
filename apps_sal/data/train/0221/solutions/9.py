class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def checkSubstrings(size):
            hashed = 0
            pow_mult = pow(26, size) % mod
            
            for i in range(size):
                hashed *= 26
                hashed += char_vals[i]
            
            hashed %= mod
            seen = {hashed}
            
            for i in range(size, len(S)):
                hashed = (hashed * 26 - char_vals[i-size] * pow_mult + char_vals[i]) % mod
                if hashed in seen:
                    return i-size+1
                seen.add(hashed)
            
            return None

        s, f = 0, len(S)
        longest = 0
        
        char_vals = [ord(c) - ord('a') for c in S]
        mod = pow(2, 63) - 1
        
        while s < f:
            m = s + (f-s+1) // 2
            longest_check = checkSubstrings(m)
            if longest_check:
                longest = longest_check
                s = m
            else:
                f = m-1
        
        return S[longest:longest+s]

