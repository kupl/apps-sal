n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(input()))
b=0
for i in a:
    b+=i.count('*')
x=y=-1
for i in range(1,n-1):
    for j in range(1,m-1):
        if a[i][j]==a[i][j-1]==a[i][j+1]==a[i-1][j]==a[i+1][j]=='*':
            x=i
            y=j
            break
if x==y==-1:
    print('NO');return
r=1
for i in range(x+1,n):
    if a[i][y]=='*':
        r+=1
    else:
        break
for i in range(x-1,-1,-1):
    if a[i][y]=='*':
        r+=1
    else:
        break
for i in range(y+1,m):
    if a[x][i]=='*':
        r+=1
    else:
        break
for i in range(y-1,-1,-1):
    if a[x][i]=='*':
        r+=1
    else:
        break
if r==b:
    print('YES')
else:
    print('NO')



        
