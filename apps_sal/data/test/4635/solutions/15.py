t=int(input())
f="abcdefghijklmnopqrstuvwxyz"
for i in range(t):
    n,k=list(map(int,input().split()))
    g=f[:k]
    s=""
    for j in range(n):
        s+=g[j%k]
    print(s)

