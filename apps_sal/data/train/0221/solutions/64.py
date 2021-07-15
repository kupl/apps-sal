class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n=len(S)
        modulus=2**56
        a=26        
        nums=[ord(c)-ord('a') for c in S]
        def search(L):
            nonlocal a,n,modulus
            aL=pow(a,L,modulus)
            h=0
            for i in range(L):
                h=(h*a+nums[i])%modulus
            seen={h}
            for start in range(1,n-L+1):
                h=(h*a-nums[start-1]*aL+nums[start+L-1])%modulus
                if h in seen:
                    return start
                seen.add(h)
            return -1
        
        l,r=1,n
        while l<=r:
            mid=(l+r)>>1
            if search(mid)!=-1:
                l=mid+1
            else:
                r=mid-1
                        
        start=search(r)        
        return S[start:start+r]
