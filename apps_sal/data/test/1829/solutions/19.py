n,m=map(int,input().split())
a=[]
b=[]
for i in range(n+m):
    a.append(input())
b=list(set(a))
if len(b)%2==1:
    if n>=m:
        print('YES')
    else:
        print('NO')
else:
    if n<=m:
        print('NO')
    else:
        print('YES')
