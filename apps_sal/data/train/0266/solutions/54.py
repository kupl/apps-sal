class Solution:
    def numSplits(self, s: str) -> int:
        p = (int)
        q = (int)
        ll = len(s)
        if ll < 2:
            return 0
        ns = len(set(s))
        np = nq = 0
        for ii in range(1,ll):
            if len(set(s[:ii])) == ns:
                np = ii
                break
        for ii in range(1,ll):
            if len(set(s[ll-ii:])) == ns:
                nq = ll-ii
                break
        if np <= nq:
            return nq-np+1
        
        ans = 0
        for ii in range(1,ll):
            p = len(set(s[:ii]))
            q = len(set(s[ii:]))
            if p == q:
                ans += 1
            elif p > q:
                return ans
                
        return ans
