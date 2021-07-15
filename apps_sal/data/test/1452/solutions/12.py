h, w = list(map(int, input().split()))
r = list(map(int, input().split()))
c = list(map(int, input().split()))

table = [[-1]*w for i in range(h)]

for i, row in enumerate(r):
    for j in range(row):
        table[i][j] = 1
    if row < w:
        table[i][row] = 0


for j, col in enumerate(c):
    for i in range(col):
        if table[i][j] == 0:
            print(0)
            return
        table[i][j] = 1
    if col < h:
        if table[col][j] == 1:
            print(0)
            return
        table[col][j] = 0

res = 1

for i in range(h):
    for j in range(w):
        if table[i][j] == -1:
            res = (res*2)%1000000007

print(res)

