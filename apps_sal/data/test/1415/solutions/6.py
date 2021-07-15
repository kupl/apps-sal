x, y, x0, y0 = map(int, input().split())

S = input()

s = []
for i in range(len(S)):
    s.append(S[i])

X = [[0 for i in range(y + 2)] for j in range(x + 2)]

for i in range(y + 2):
    X[0][i] = -1
    X[x + 1][i] = -1

for i in range(x + 2):
    X[i][0] = -1
    X[i][y + 1] = -1


X[x0][y0] = 1
result = [1]
nr_explore = 1

for move in s:
    dx = 0
    dy = 0
    if move == 'U':
        dx = -1
        dy = 0
    elif move == 'D':
        dx = 1
        dy = 0
    elif move == 'R':
        dx = 0
        dy = 1
    elif move == 'L':
        dx = 0
        dy = -1

    if X[x0 + dx][y0 + dy] != -1:
        x0 += dx
        y0 += dy
        if X[x0][y0] == 0:
            nr_explore += 1
            X[x0][y0] = 1
            result.append(1)
        else:
            result.append(0)
    else:
        result.append(0)

result[-1] += x * y - nr_explore
for r in result:
    print(r, end=" ")

