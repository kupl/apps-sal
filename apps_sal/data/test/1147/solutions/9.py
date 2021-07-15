from bisect import bisect_left
R=lambda:map(int,input().split())
n,m,k=R()
a=sorted(R())
s=0
for i in a:
    l = ((i - 1) // m + k) * m
    s+=bisect_left(a,l+m)-bisect_left(a,max(i,l))
print(s)
