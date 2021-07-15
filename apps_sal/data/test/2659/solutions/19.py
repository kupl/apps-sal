k=int(input())
A=[]
for i in range(1,9):
    A.append([i,1])
now=0
for i in range(15):
    now+=9*10**i
    for j in range(1000):
        c=now+j*10**(i+1)
        S=str(c)
        cnt=0
        for s in S:
            cnt+=int(s)
        A.append([c,c/cnt])
A=list(reversed(sorted(A)))
now=0
m=A[0][1]
Ans=[]
for a in A:
    if a[0]==now:
        continue
    else:
        now=a[0]
        if a[1]<=m:
            Ans.append(now)
            m=a[1]
Ans=list(reversed(Ans))
for i in range(k):
    print(Ans[i])
