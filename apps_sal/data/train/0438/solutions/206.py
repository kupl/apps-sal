class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def func(i):
            if d[i]!=i: d[i]=func(d[i])
            return d[i]
        d,dd,a,s={},{},{},-1
        for p,i in enumerate(arr,1):
            if i-1 in d:
                if i+1 in d:
                    j,k=func(i-1),func(i+1)
                    d[k],d[i]=j,j
                    a[dd[j]]-=1
                    a[dd[k]]-=1
                    dd[j]+=dd[k]+1
                    a[dd[j]]=a.get(dd[j],0)+1
                else:
                    j=func(i-1)
                    d[i]=j
                    a[dd[j]]-=1
                    dd[j]+=1
                    a[dd[j]]=a.get(dd[j],0)+1
            elif i+1 in d:
                j=func(i+1)
                d[i]=j
                a[dd[j]]-=1
                dd[j]+=1
                a[dd[j]]=a.get(dd[j],0)+1
            else:
                d[i]=i
                dd[i]=1
                a[1]=a.get(1,0)+1
            if a.get(m,0): s=p
        return s
