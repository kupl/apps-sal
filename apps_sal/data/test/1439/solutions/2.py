from copy import deepcopy
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
if n > m:
    print('YES')
else:
    d = [False for i in range(m)]
    b = [False for i in range(m)]
    for i in range(n):
        for j in range(m):
            if d[j] == True:
                b[(j + a[i]) % m] = True
        b[a[i] % m] = True
        for j in range(m):
            if b[j] == True:
                d[j] == True
        d = deepcopy(b)
    if d[0] == True:
        print('YES')
    else:
        print('NO')

