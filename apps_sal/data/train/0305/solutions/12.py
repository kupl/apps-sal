class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        mod = 1_000_000_007
        # Dict for storing hashes for all substrings
        hashed = {}
        for i in range(len(text)):
            sm = 0
            for j in range(i, len(text)):
                sm = (sm*128 + ord(text[j]))%mod
                hashed[(i, j)] = sm
        
        ans = 0
        st = {}
        for i in range(len(text)):
            for j in range(i+1, len(text), 2):
                # For each even length substring check if hash of first half
                # matches the hash of second half
                # Also check if the full string already exists as stored map
                if hashed[(i, i-1+(j + 1 - i)//2)] == hashed[(i+(j + 1 - i)//2, j)]:
                    if hashed[(i, j)] not in st:
                        ans += 1
                        st[hashed[(i,j)]] = 1
        return ans
