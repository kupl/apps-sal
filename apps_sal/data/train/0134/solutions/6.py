def f(n,s,e,ci,di,v):
    if n==ci:
        return 1
    a=0
    if (e,ci,v) in di:
        return di[e,ci,v]
    for i in range(10):
            if e==0:
                if not v>>i&1:
                    eee=v|(1<<i)
                    a+=f(n,s,0,ci+1,di,eee)
            else:
                if i>int(s[ci]):
                    break
                if int(s[ci])==i:
                    if not v>>i&1:
                        eee=v|(1<<i)
                        a+=f(n,s,1,ci+1,di,eee)
                    break
                if not v>>i&1:
                    eee=v|(1<<i)
                    a+=f(n,s,0,ci+1,di,eee)
    di[e,ci,v]=a
    return a
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        if n<=10:
            return 0
        s=str(n)
        l=len(s)
        ans=10
        prev=9
        for i in range(9,9-l+2,-1):
            ans+= prev*i
            prev=prev*i
        a=0
        di={}
        v=0
        for i in range(1,10):
            if i>int(s[0]):
                break
            if i==int(s[0]):
                e=1<<i
                a+=f(l,s,1,1,di,e)
                break
            e=1<<i
            a+=f(l,s,0,1,di,e)
        return n-a-ans+1

