L = list(map(int,input().split()))
N = len(L)


S= sum(L)
for bit in range(1<<N):
    t=0
    for i in range(N):
        if bit>>i&1:
            t+=L[i]
    if S-t==t:
        print("Yes")
        return
print("No")

