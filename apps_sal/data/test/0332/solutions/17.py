n,m=[int(x) for x in input().split()]
A=[]
B=[]
for i in range(n):
    a=[int(x) for x in input().split()]
    A.append(a)
for i in range(n):
    a=[int(x) for x in input().split()]
    B.append(a)
a_list=[]
for i in range(n):
    a=[]
    j=0
    a.append(A[i][j])
    while 1:
        if i-1>=0 and j+1<=m-1:
            i-=1
            j+=1
            a.append(A[i][j])
        else:
            break
    a_list.append(a)
i=n-1
for j in range(1,m):
    i=n-1
    a=[]
    a.append(A[i][j])
    while 1:
        if i-1>=0 and j+1<=m-1:
            i-=1
            j+=1
            a.append(A[i][j])
        else:
            break
    a_list.append(a)
    
b_list=[]
for i in range(n):
    a=[]
    j=0
    a.append(B[i][j])
    while 1:
        if i-1>=0 and j+1<=m-1:
            i-=1
            j+=1
            a.append(B[i][j])
        else:
            break
    b_list.append(a)
i=n-1
for j in range(1,m):
    a=[]
    i=n-1
    a.append(B[i][j])
    while 1:
        if i-1>=0 and j+1<=m-1:
            i-=1
            j+=1
            a.append(B[i][j])
        else:
            break
    b_list.append(a)
for i in range(len(a_list)):
    a=sorted(a_list[i])
    b=sorted(b_list[i])
    if a!=b:
        print('NO')
        break
else:
    print('YES')

