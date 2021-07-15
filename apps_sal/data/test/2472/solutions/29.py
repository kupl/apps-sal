N=int(input())
A=[list(map(int,input().split())) for i in range(N)]
A=sorted(A,key=lambda x:x[1])
S=0
T=True
for i in range(N):
    S+=A[i][0]
    if A[i][1]<S:
        T=False
if T==True:
    print("Yes")
else:
    print("No")
