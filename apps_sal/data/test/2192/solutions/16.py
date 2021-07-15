n=int(input())
inData=[]
for i in range(n):
    x=list(map(int,input().split(" ")))
    inData.append(x)
A=[list(range(n)) for i in range(n)]
B=[list(range(n)) for i in range(n)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            A[i-1][j-1]=inData[i-1][j-1]
            B[i-1][j-1]=0
        else:
            A[i-1][j-1]=(inData[i-1][j-1]+inData[j-1][i-1])/2
            B[i-1][j-1]=(inData[i-1][j-1]-inData[j-1][i-1])/2
            
for i in range(n):
    for j in range(n):
        print(str(A[i][j])+" ",end="")
    print()

for i in range(n):
    for j in range(n):
        print(str(B[i][j])+" ",end="")
    print()

