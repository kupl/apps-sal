n, k = map(int, input().split())
mapp = [list(input()) for i in range(n)]
res = 0
res = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    count = 0
    for j in range(n):
        if (mapp[i][j] == '.'):
            count += 1
        else:
            count = 0
        if (count >= k):
            for t in range(j - k + 1, j + 1):
                res[i][t] += 1

for i in range(n):
    count = 0
    for j in range(n):
        if (mapp[j][i] == '.'):
            count += 1
        else:
            count = 0
        if (count >= k):
            for t in range(j - k + 1, j + 1):
                res[t][i] += 1
ress = [0, 0]
maxx = -1
for i in range(n):
    for j in range(n):
        if (maxx < res[i][j]):
            maxx = res[i][j]
            ress[0], ress[1] = i + 1, j + 1
print(*ress)
