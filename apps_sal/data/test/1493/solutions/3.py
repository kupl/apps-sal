(n, m) = list(map(int, input().split()))
field = [list(input()) for i in range(n)]
s1 = ''.join(('BW' for i in range(m // 2 + 1)))[:m]
s2 = ''.join(('WB' for i in range(m // 2 + 1)))[:m]
res = []
for i in range(n):
    res.append([])
    for j in range(m):
        if field[i][j] == '.':
            if i % 2 == 0:
                res[i].append(s1[j])
            else:
                res[i].append(s2[j])
        else:
            res[i].append('-')
for i in range(n):
    print(''.join(res[i]))
