r, c = (int(x) for x in input().split())

g = []
for i in range(r):
    g.append(input())


def fn():
    for rr in range(r):
        for cc in range(c):
            if g[rr][cc] != 'W':
                continue
            if cc > 0 and g[rr][cc - 1] == 'S':
                return False
            if cc < c - 1 and g[rr][cc + 1] == 'S':
                return False
            if rr > 0 and g[rr - 1][cc] == 'S':
                return False
            if rr < r - 1 and g[rr + 1][cc] == 'S':
                return False
    return True


res = fn()
if not res:
    print('No')
else:
    print('Yes')
    for row in g:
        print(row.replace('.', 'D'))
