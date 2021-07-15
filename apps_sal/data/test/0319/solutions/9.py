m,n=list(map(int,input().split()))
a=[]
for i in range(m):
    a.append(list(map(int,list(input()))))
b=[0]*n
for j in range(n):
    b[j]=0
    for i in range(m):
        b[j]+=a[i][j]
for i in range(m):
    for j in range(n):
        if(b[j]==a[i][j]):
            break
    else:
        print("YES")
        break
else:
    print("NO")
