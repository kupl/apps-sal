class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        spl = list(s)
        n = len(spl)
        c = collections.Counter(spl)
        if all(v==1 for v in c.values()):
            return n
        mx = 2**(n-1)-2
        ans = 1
        for cmb in range(mx,0,-1):            
            bs = list(bin(cmb)[2:].zfill(n-1))
            if bs.count('1')+1<ans:
                #if cmb<2**10:
                    #print(cmb,bs)
                continue
            spl = []
            sub = s[0]
            for i,b in enumerate(bs):
                if b=='0':
                    sub += s[i+1]
                else:
                    spl.append(sub)
                    sub = s[i+1]
            spl.append(sub)
            c = collections.Counter(spl)
            if all(v==1 for v in c.values()):
                if len(spl)>ans:
                    ans = len(spl)
                    #print(n,cmb,ans,spl)
        return ans
