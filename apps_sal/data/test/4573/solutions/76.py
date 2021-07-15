n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
k,l=y[n//2-1],y[n//2]
for i in range(n):
    if x[i]<=k:
        print(l)
    else:
        print(k)
