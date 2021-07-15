A=list(map(int,input().split()))
can=False
for bit in range (2**4):
    eat=int(0)
    uneat=int(0)
    for i in range (4):
        if bit & (1<<i):
            eat+=A[i]
        else :
            uneat+=A[i]
    if eat==uneat:
        can=True
if can:
    print("Yes")
else :
    print("No")
