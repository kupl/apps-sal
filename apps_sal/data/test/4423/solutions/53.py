N=int(input())
x=[]
for i in range(N):
    S,P=map(str,input().split())
    x.append([S,int(P),i+1])
X=sorted(x,key=lambda x:(x[0],-x[1]))
for i in range(N):
    print(X[i][2])
