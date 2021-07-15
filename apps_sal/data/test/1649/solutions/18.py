ans=False
A=list(map(int,input().split()))

for bit in range(1,2**4):
    a=int(0)
    b=int(0)
    for i in range(4):
        if bit & (1<<i):
            a+=A[i]
        else:
            b+=A[i]
    if a==b:
        ans=True
if ans:
    print('Yes')
else:
    print('No')
