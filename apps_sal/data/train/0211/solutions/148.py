class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        c=collections.Counter(s)
        #print(c,c.keys(),len(c.keys()))
        res=len(c.keys())
        l=len(s)
        ways=int(math.pow(2,l-1))
        for i in range(ways):
            bit=str(bin(i))[2:].zfill(l-1)
            #print(bit)
            cand=[s[0]]
            for i,x in enumerate(bit):
                if x=='0':
                    cand[-1]+=s[i+1]
                else:
                    cand.append(s[i+1])
            #cand[-1]+=s[-1]
            #print(cand)
            nodup=set(cand)
            if len(nodup)==len(cand):
                res=max(res,len(cand))
        return res
