from copy import deepcopy

n, m = list(map(int, input().split()))
pole = []
x, y = 0, 0
count = 0
for i in range(n):
    s = input()
    pole.append(s)
    for j in range(len(s)):
        if s[j] == '*':
            count += 1
        if s[j] == 'S':
            x = i
            y = j

X = [0, -1, 0, 1]
Y = [-1, 0, 1, 0]

d = dict()
d[0] = 'L'
d[1] = 'U'
d[2] = 'R'
d[3] = 'D'

prevx, prevy = -1, -1

xbegin, ybegin = deepcopy(x), deepcopy(y)
s = ''
now = 0
for i in range(n):
    for j in range(m):
        for u in range(4):
            if x + X[u] >= 0 and x + X[u] < n and y + Y[u] >= 0 and y + Y[u] < m:
                if pole[x + X[u]][y + Y[u]] == '*' and (x + X[u] != prevx or y + Y[u] != prevy):
                    prevx, prevy = deepcopy(x), deepcopy(y)
                    x += X[u]
                    y += Y[u]
                    s += d[u]
                    count -= 1
                    break
        if count == -1:
            break
    if count == -1:
        break
if x - 1 >= 0 and pole[x - 1][y] == 'S':
    s += 'U'
if x + 1 < n and pole[x + 1][y] == 'S':
    s += 'D'
if y - 1 >= 0 and pole[x][y - 1] == 'S':
    s += 'L'
if y + 1 < m and pole[x][y + 1] == 'S':
    s += 'R'
print(s)
