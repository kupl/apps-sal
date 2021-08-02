R, C = list(map(int, input().split()))
r = []
f = 0
for i in range(R):
    r.append(input())
    for j in range(C):
        if r[i][j] == 'W':
            if j and r[i][j - 1] == 'S':
                f = 1
                break
            if j + 1 < C and r[i][j + 1] == 'S':
                f = 1
                break
    if f:
        break
if not f:
    for i in range(C):
        for j in range(R):
            if r[j][i] == 'W':
                if j and r[j - 1][i] == 'S':
                    f = 1
                    break
                if j + 1 < R and r[j + 1][i] == 'S':
                    f = 1
                    break
        if f:
            break
if f:
    print('No')
else:
    print('Yes')
    for i in range(R):
        print(r[i].replace('.', 'D'))
