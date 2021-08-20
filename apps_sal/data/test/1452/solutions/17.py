(h, w) = list(map(int, input().split()))
rows = list(map(int, input().split()))
cols = list(map(int, input().split()))
matrix = [None] * h
answer = 0
found = False
for i in range(h):
    matrix[i] = [-1] * w
for i in range(h):
    r = rows[i]
    if r == 0:
        matrix[i][0] = 0
    else:
        for j in range(r):
            matrix[i][j] = 1
        if r < w:
            matrix[i][r] = 0
for i in range(w):
    c = cols[i]
    if c == 0:
        if matrix[0][i] == 1:
            found = True
        matrix[0][i] = 0
    else:
        for j in range(c):
            if matrix[j][i] == 0:
                found = True
                break
            matrix[j][i] = 1
        if c < h:
            if matrix[c][i] == 1:
                found = True
            matrix[c][i] = 0
if not found:
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] < 0:
                cnt += 1
    answer = 2 ** cnt % 1000000007
print(answer)
