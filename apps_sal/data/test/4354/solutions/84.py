n,m=map(int,input().split())
A=[]
B=[]
C=[]
D=[]
E=[]
ans=0
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(m):
    c,d=map(int,input().split())
    C.append(c)
    D.append(d)
for i in range(n):
    for j in range(m):
        ans = abs(A[i]-C[j])+abs(B[i]-D[j])
        E.append(ans)
        ans=0
    print(E.index(min(E))+1)
    E.clear()
