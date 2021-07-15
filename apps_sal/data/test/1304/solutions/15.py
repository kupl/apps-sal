a=[]
for i in range(11):
    b=[]
    s=input().split()
    if not s:
        continue
    for k in s:
        for i in range(3):
            b.append(k[i])
    a.append(b)
x,y=map(int,input().split())
x=(x-1)%3
y=(y-1)%3
fl=False
for i in range(x*3,x*3+3):
    for j in range(y*3,y*3+3):
        if a[i][j]=='.':
            a[i][j]='!'
            fl=True
if not fl:
    for i in range(9):
        for j in range(9):
            if a[i][j]=='.':
                a[i][j]='!'
for i in range(3):
    for j in range(3):
        for k in range(3):
            for c in range(3):
                print(a[i*3+j][k*3+c],end='')
            print(' ',end='')
        print()
    print()

