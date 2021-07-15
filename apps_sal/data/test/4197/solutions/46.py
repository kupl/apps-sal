N=int(input())
A=list(map(int,input().split()))
a=[0]*N
for i in range(N):
    a[A[i]-1]=i+1

for i in range(N-1):
    print(a[i],end=' ')
print(a[N-1])
