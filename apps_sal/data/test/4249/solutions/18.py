def check(sz):
        aa=0
        for i in range(n):
                aa+=max(0,a[i]-i//sz)
                if aa>=M:
                        return True
        return False 
n,M=map(int,input().split())
a=list(map(int,input().split()))
if sum(a)<M:print(-1);return
a.sort(reverse=True)
l=1;r=n
while l<r:
        m=l+r
        m>>=1
        if check(m):
                r=m
        else:
                l=m+1
print(l)
