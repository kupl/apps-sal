(h, w) = [int(x) for x in input().split()]
m = [['.'] * (w + 2)]
for i in range(h):
    m.append(['.'] + list(input()) + ['.'])
m.append(m[0])


def check(x, y):
    res = 0
    for i in range(3):
        for j in range(3):
            if m[x - 1 + i][y - 1 + j] == '#':
                res += 1
    return str(res)


for i in range(1, h + 1):
    for j in range(1, w + 1):
        if m[i][j] == '.':
            m[i][j] = check(i, j)
ans = []
for i in range(h):
    ans.append(m[i + 1][1:w + 1])
for i in range(h):
    print(''.join(ans[i]))
