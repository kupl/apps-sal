def isValid(field, y, x):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if field[y + i][x + j] == '.':
                return False
    return True


def fill(field, y, x):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            cur[y + i][x + j] = '#'


n, m = list(map(int, input().split()))
sig = []
cur = []
for i in range(n):
    sig += [list(input())]
    cur += [["."] * m]

for i in range(n - 2):
    for j in range(m - 2):
        if isValid(sig, i, j):
            fill(cur, i, j)

if sig == cur:
    print("YES")
else:
    print("NO")
