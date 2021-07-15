A=list(map(int,input().split()))
n=int(4)

can=False
for bit in range(2**n):
    all=int(0)
    for i in range(n):
        if bit & (1<<i):
            all+=A[i]
    if 2*all==sum(A):
        can=True
if can:
    print('Yes')
else:
    print('No')
