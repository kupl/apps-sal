(h, w) = map(int, input().split())
field = [input() for i in range(h)]
q = int(input())
inrow = [[0] * (w + 1) for i in range(h + 1)]
for i in range(h):
    sum = 0
    for j in range(1, w):
        if field[i][j] == field[i][j - 1] == '.':
            sum += 1
        inrow[i][j] = sum
incol = [[0] * (h + 1) for i in range(w + 1)]
for j in range(w):
    sum = 0
    for i in range(1, h):
        if field[i][j] == field[i - 1][j] == '.':
            sum += 1
        incol[j][i] = sum
suminrows = [[0] * (w + 1) for i in range(h + 1)]
for j in range(w):
    sum = 0
    for i in range(h):
        sum += inrow[i][j]
        suminrows[i][j] = sum
sumincols = [[0] * (h + 1) for i in range(w + 1)]
for i in range(h):
    sum = 0
    for j in range(w):
        sum += incol[j][i]
        sumincols[j][i] = sum
for test in range(q):
    (r1, c1, r2, c2) = map(int, input().split())
    (r1, c1, r2, c2) = (r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    ans = 0
    ans += suminrows[r2][c2] - suminrows[r1 - 1][c2] - (suminrows[r2][c1] - suminrows[r1 - 1][c1])
    ans += sumincols[c2][r2] - sumincols[c1 - 1][r2] - (sumincols[c2][r1] - sumincols[c1 - 1][r1])
    print(ans)
