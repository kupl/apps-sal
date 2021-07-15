import sys
N, M= map(int, input().split())
x = list(map(int, input().split()))
X=sorted(x)
D=[0]*(M-1)
if N>=M:
    print(0)
    return
for i in range(M-1):
    D[i]=X[i+1]-X[i]
new_D = sorted(D)
cnt=0
for i in range(M-N):
    cnt=cnt+new_D[i]
print(cnt)
