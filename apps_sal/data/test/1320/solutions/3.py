n = int(input())
(g, r, c) = ([input() for i in range(n)], [0] * n, [0] * n)
for i in range(n):
    for j in range(n):
        if g[i][j] == 'C':
            r[i] += 1
            c[j] += 1
print(sum((x * (x - 1) // 2 for x in r + c)))
