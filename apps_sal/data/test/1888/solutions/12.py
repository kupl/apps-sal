
n, m = list(map(int, input().split()))
abc = [list(map(int, input().split())) for i in range(m)]

mat = [[0] * n for i in range(n)]
for t in abc:
    mat[t[0] - 1][t[1] - 1] = t[2]

total = 0
for i in range(n):
    s = sum(mat[i][:]) - sum([mat[x][i] for x in range(n)])
    if s < 0:
        continue
    total += s
print(total)
