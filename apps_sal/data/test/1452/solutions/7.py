h, w = list(map(int, input().split()))

r = list(map(int, input().split()))
c = list(map(int, input().split()))

unset = h * w

field = [[-1] * w for _ in range(h)]

for i in range(h):
    x = r[i]
    row = field[i]
    for j in range(x):
        if row[j] == -1:
            unset -= 1
        row[j] = 1
    if x < w:
        if row[x] == -1:
            unset -= 1
        row[x] = 0

for i in range(w):
    x = c[i]
    for j in range(x):
        if field[j][i] == -1:
            unset -= 1
        elif field[j][i] == 0:
            print(0)
            return
        field[j][i] = 1
    if x < h:
        if field[x][i] == -1:
            unset -= 1
        elif field[x][i] == 1:
            print(0)
            return
        field[x][i] = 0

print(pow(2, unset, 10 ** 9 + 7))
