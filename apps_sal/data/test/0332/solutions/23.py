n,m = list(map(int, input().strip().split()))
a = []
b = []
for i in range(n):
    l = list(map(int, input().strip().split()))
    a.append(l)
for i in range(n):
    l = list(map(int, input().strip().split()))
    b.append(l)
test = True
for i in range(n+m-1):
    c = []
    d = []
    if i < m-1:
        for j in range(i,-1,-1):
            c.append(a[i-j][j])
            d.append(b[i-j][j])
            if i-j == n-1:
                break
        c.sort()
        d.sort()
        if c!= d:
            test = False
            break
    else:
        x = i- (m-1)
        for j in range(x,n):
            c.append(a[j][m-1-(j-x)])
            d.append(b[j][m-1-(j-x)])
            if m-1-(j-x) == 0:
                break
        c.sort()
        d.sort()
        if c!= d:
            test = False
            break
if test == True:
    print('YES')
else:
    print('NO')

