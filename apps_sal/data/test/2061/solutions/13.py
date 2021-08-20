import sys
sys.setrecursionlimit(100000)
(n, m, k) = map(int, input().split())
arr = []
for i in range(n):
    krr = []
    p = input()
    for x in p:
        if x == '*':
            krr.append(0)
        else:
            krr.append(-1)
    arr.append(krr)
lakes = [-1]
islakes = [-1]
lakesp = [[-1, -1]]


def go(x, y, c):
    if x < 0 or x >= n or y < 0 or (y >= m):
        return
    if arr[x][y] == 0:
        return
    if arr[x][y] != -1:
        return
    arr[x][y] = c
    if x == 0 or x == n - 1 or y == 0 or (y == m - 1):
        islakes[c] = 0
    lakes[c] += 1
    go(x - 1, y, c)
    go(x, y - 1, c)
    go(x + 1, y, c)
    go(x, y + 1, c)


color = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == -1:
            color += 1
            lakes.append(0)
            islakes.append(1)
            go(x, y, color)
            lakesp.append([x, y])


def re(x, y):
    if x < 0 or x >= n or y < 0 or (y >= m):
        return
    if arr[x][y] == 0:
        return
    arr[x][y] = 0
    re(x - 1, y)
    re(x, y - 1)
    re(x + 1, y)
    re(x, y + 1)


def min():
    min = 1000000000
    mini = 0
    for i in range(1, color + 1):
        if islakes[i]:
            if min > lakes[i]:
                min = lakes[i]
                mini = i
    return mini


cnt = 0
nn = 0
for i in range(1, color + 1):
    if islakes[i] == 0:
        continue
    nn += 1
p = nn - k
for i in range(1, color + 1):
    if p == 0:
        break
    j = min()
    cnt += lakes[j]
    lakes[j] = 1000000000
    re(lakesp[j][0], lakesp[j][1])
    p -= 1
print(cnt)
for x in arr:
    s = ''
    for y in x:
        if y == 0:
            s += '*'
        else:
            s += '.'
    print(s)
