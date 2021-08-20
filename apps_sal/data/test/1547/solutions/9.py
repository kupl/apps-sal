(n, m, k) = map(int, input().split())
columns = [[0] * 2 for i in range(n)]
strokes = [[0] * 2 for i in range(m)]
for i in range(n):
    columns[i][1] = -1
for i in range(m):
    strokes[i][1] = -1
for i in range(k):
    (num, rci, ai) = map(int, input().split())
    if num == 2:
        strokes[rci - 1][0] = ai
        strokes[rci - 1][1] = i
    else:
        columns[rci - 1][0] = ai
        columns[rci - 1][1] = i
nm = [[[0] * 2 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if columns[i][1] >= nm[i][j][1]:
            nm[i][j][0] = columns[i][0]
            nm[i][j][1] = columns[i][1]
        if strokes[j][1] >= nm[i][j][1]:
            nm[i][j][0] = strokes[j][0]
            nm[i][j][1] = strokes[j][1]
for i in range(n):
    for j in range(m):
        print(nm[i][j][0], end=' ')
    print()
