N,K=map(int,input().split())
A=[]
people=list(range(1,N+1,1))
for idx in range(K):
    d=int(input())
    X=list((map(int,input().split())))
    for i in range(len(X)):
        A.append(X[i])
ans =[i for i in people if not i in A]
print(len(ans))
