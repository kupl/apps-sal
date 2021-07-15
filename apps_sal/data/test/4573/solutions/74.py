N=int(input())
X=list(map(int,input().strip().split()))

Y=sorted(X)
a=Y[N//2-1]
b=Y[N//2]
for n in range(N):
    if X[n]<=a:
        print(b)
    else:
        print(a)
