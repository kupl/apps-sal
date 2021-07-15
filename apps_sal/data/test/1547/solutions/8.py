n, m, k = map(int, input().split())
stol = [[0, -1] for i in range(m)]
strok = [[0, -1] for i in range(n)]
for i in range(k):
    c, ri, ai = map(int, input().split())
    if c == 1:
        strok[ri - 1][0] = ai
        strok[ri - 1][1] = i
    else:
        stol[ri - 1][0] = ai
        stol[ri - 1][1] = i
data = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if strok[i][1] > stol[j][1]:
            data[i][j] = strok[i][0]
        else:
            data[i][j] = stol[j][0]
for i in range(n):
    print(*data[i])
