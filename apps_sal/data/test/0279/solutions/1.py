ninf = -500000

u, v = list(map(int, input().split(' ')))
t, d = list(map(int, input().split(' ')))

l = [[ninf] * 1201 for _ in range(2)]

l[0][u] = u

for i in range(1, t):
    for j in range(1201):
        l[i & 1][j] = max(l[~i & 1][max(0, j - d): min(1200, j + d) + 1]) + j

print(l[(t - 1) & 1][v])
