r,p=range,print
n,a,b=map(int,input().split())
if a+b>n+1or a*b<n:print(-1);return
l=[[]for i in r(b-1)]+[list(r(1,a+1))]
for i in r(a+1,n+1):l[-2-(i-a-1)%(b-1)]+=[i]
for i in l:p(*i,end=" ")
