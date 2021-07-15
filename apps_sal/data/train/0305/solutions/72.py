class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        nums = [ord(c) - ord('a') for c in text]
        
        def countEcho(L):
            '''
            count echo substrings with length L
            '''
            
            a = 26
            modulus = 2**32
            
            h1 = h2 = 0
            for i in range(L):
                h1 = (h1*a + nums[i]) % modulus
                h2 = (h2*a + nums[L+i]) % modulus
            # print(L, h1, h2)
            seen = set()
            ans = 0
            if h1 == h2:
                ans += 1
                seen.add(h1)
            aL = pow(a, L, modulus)
            for i in range(1, n - 2*L + 1):
                h1 = (h1 * a - nums[i-1] * aL + nums[i+L-1]) % modulus
                h2 = (h2 * a - nums[i+L-1] * aL + nums[i+L*2-1]) % modulus
                # print(L, h1, h2)
                if h1 == h2 and h1 not in seen:
                    ans += 1
                    seen.add(h1)
            return ans
        
        ans = 0
        for L in range(1, n//2+1):
            al = countEcho(L)
            ans += al
        return ans
