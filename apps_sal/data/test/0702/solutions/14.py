def mp():
    return map(int, input().split())

n = int(input())
a = [[j for j in input()] for i in range(n)]

fail = False
for i in range(n):
    for j in range(n):
        if a[i][j] == '#':
            continue
        if (i + 1 < n and a[i + 1][j] == '.') and (i + 2 < n and a[i + 2][j] == '.') and (i + 1 < n and j + 1 < n and a[i + 1][j + 1] == '.') and (i + 1 < n and j - 1 >= 0 and a[i + 1][j - 1] == '.'):
            a[i][j] = '#'
            a[i + 1][j] = '#'
            a[i + 2][j] = '#'
            a[i + 1][j + 1] = '#'
            a[i + 1][j - 1] = '#'
        else:
            fail = True
        
    if fail:
        break
    
for i in a:
    for j in i:
        if j != '#':
            fail = True
            break

if fail:
    print('NO')
else:
    print('YES')
