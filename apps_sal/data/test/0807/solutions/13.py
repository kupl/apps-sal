n,c=list(map(int,input().split()))

A=list(map(int,input().split()))
best=0
for i in range(n-1):
    if(A[i]-A[i+1]>best):
        best=A[i]-A[i+1]
print(max(0,best-c))

