n, m = [int(x) for x in input().split()]
s = []
for i in range(n):
    s.append(input())
mapp = [[False] * m for i in range(n)]


rnd = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def gene(x, y, p):
    cx = x - rnd[p][0]
    cy = y - rnd[p][1]
    ans = []
    for i in range(8):
        ans.append((cx + rnd[i][0], cy + rnd[i][1]))
    return ans


def judge(ps):
    for x, y in ps:
        if x >= 0 and x < n and y >= 0 and y < m and s[x][y] == '#':
            continue
        else:
            return False
    return True


def dye(ps):
    nonlocal mapp
    for x, y in ps:
        mapp[x][y] = True


def check(x, y):
    for i in range(8):
        r = gene(x, y, i)
        if judge(r):
            dye(r)
            return True
    return False


for i in range(n):
    for j in range(m):
        if s[i][j] == '#' and mapp[i][j] == False:
            if check(i, j):
                continue
            else:
                print('NO')
                quit()
print('YES')
