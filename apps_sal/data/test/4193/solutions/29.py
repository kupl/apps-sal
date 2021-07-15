A=[list(map(int,input().split())) for i in range(3)]
n=int(input())
b=[int(input()) for i in range(n)]
for i in range(3):
    for j in range(3):
        for k in range(n):
            if A[i][j]==b[k]:
                A[i][j]=-1
if A[0][0]==-1 and A[1][1]==-1 and A[2][2]==-1:
    print("Yes")
    return
elif A[0][2]==-1 and A[1][1]==-1 and A[2][0]==-1:
    print("Yes")
    return
for i in range(3):
    total=0
    if A[i].count(-1)==3:
        print("Yes")
        return
    for j in range(3):
        if A[j][i]==-1:
            total+=1
    if total==3:
        print("Yes")
        return
print("No")
