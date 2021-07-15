class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        a={}
        def check(n,a):
            ct=0
            while n!=1:
                if n%2==0:
                    n=n/2
                else:
                    n=3*n+1
                if n in a:
                    ct += a[n]+1
                    return ct
                    break
                ct +=1
            return ct
        for i in range(lo,hi+1):
            a[i] = check(i,a)
        b=sorted(a.items(), key=lambda kv:(kv[1],kv[0]))
        return b[k-1][0]
