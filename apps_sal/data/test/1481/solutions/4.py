n=int(input())
desk=[input() for i in range(n)]
fl=True
for i in range(n):
    for g in range(n):
        a=0
        if g-1>=0:
            if desk[i][g-1]=='o':
                a+=1
        if g+1<n:
            if desk[i][g+1]=='o':
                a+=1
        if i-1>=0:
            if desk[i-1][g]=='o':
                a+=1
        if i+1<n:
            if desk[i+1][g]=='o':
                a+=1
        if a%2!=0:
            fl=False
            break
    if not fl:
        print('NO')
        break
if fl:
    print('YES')
