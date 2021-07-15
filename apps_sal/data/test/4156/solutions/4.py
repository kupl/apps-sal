n,m=map(int,input().split())
a=list(map(int,input().split()))
mi=0
ma=0
k=0
for i in range(n):
    k+=a[i]
    if k>ma:
        ma=k
    if k<mi:
        mi=k
if m-ma+mi+1<0:
    print(0)
else:
    print(m-ma+mi+1)
