N,A,B,C=list(map(int,input().split()))
l=[]
for i in range(N):
    l.append(int(input()))

from itertools import product

P=product(list(range(4)),repeat=N)

ans=1000000000
for p in P:
    A_len=0
    B_len=0
    C_len=0
    temp=0
    for i in range(N):
        n=int(p[i])
        if n==3:
            if A_len!=0:
                temp+=10
            A_len+=l[i]
        elif n==2:
            if B_len!=0:
                temp+=10
            B_len+=l[i]
        elif n==1:
            if C_len!=0:
                temp+=10
            C_len+=l[i]

    if A_len!=0 and B_len!=0 and C_len!=0:
        temp+=abs(A-A_len)
        temp+=abs(B-B_len)
        temp+=abs(C-C_len)

        ans=min(ans,temp)

print(ans)


