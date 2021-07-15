class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def test(L):
            base = 26
            modulus = 2**32
            AL = base**L%modulus
            hk = 0
            for i in range(L):
                hk=hk*base+nums[i]
            hk%=modulus
            hs=set([hk])
            
            for i in range(L, len(S)):
                hk = hk*base-nums[i-L]*AL+nums[i]
                hk%=modulus
                if hk in hs:
                    return i-L+1
                hs.add(hk)
        
        nums = [ord(c)-ord('a') for c in S]
        start, end = 1, len(S)
        res = -1
        while start<=end:
            mid = start+(end-start)//2
            pos = test(mid)
            
            if pos:
                res = pos
                start = mid+1
            else:
                end = mid-1
            
        return S[res:res+end]
