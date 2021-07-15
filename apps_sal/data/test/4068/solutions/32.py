N,M=map(int,input().split())
a=[0]
for i in range(0,M):
    a.append(int(input()))
a.append(N+1)
b=[0]*(N+2)
b[0]=0
b[1]=1
for j in range(0,M+1):
    for i in range(a[j]+2,a[j+1]+1):
        b[i]=(b[i-1]+b[i-2])%1000000007

print(b[N+1])
