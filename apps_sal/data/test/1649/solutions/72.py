from itertools import product
l=list(map(int,input().split()))
bit=list(product([0,1],repeat=len(l)))
for i in range(len(bit)):
    SUM=0
    for j in range(len(l)):
        SUM+=l[j]*bit[i][j]
    if (SUM==sum(l)-SUM):
        print("Yes")
        return
else:
    print("No")
