n, m = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = list(input())
g1 = '*
g2 = 'qwertyuiopasdfghjklzxcvbnm'
g3 = '1234567890'

b = [[-1] * 3 for i in range(n)]

for i in range(n):
    f1, f2, f3 = 0, 0, 0
    for j in range(m):
        if a[i][j] in g1 and f1 == 0:
            f1 = 1
            b[i][0] = j
        elif a[i][j] in g2 and f2 == 0:
            f2 = 1
            b[i][1] = j
        elif a[i][j] in g3 and f3 == 0:
            f3 = 1
            b[i][2] = j

    f1, f2, f3 = 0, 0, 0
    for j in range(-1, -1 * m, -1):
        if a[i][j] in g1 and f1 == 0:
            f1 = 1
            b[i][0] = min(b[i][0], -1 * j)
        elif a[i][j] in g2 and f2 == 0:
            f2 = 1
            b[i][1] = min(b[i][1], -1 * j)
        elif a[i][j] in g3 and f3 == 0:
            f3 = 1
            b[i][2] = min(b[i][2], -1 * j)

ans = int(1e9)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            for l in range(3):
                for g in range(3):
                    for q in range(3):
                        if q != l and l != g and q != g and b[i][l] + b[j][g] + b[k][q] < ans and b[i][l] != -1 and b[j][g] != -1 and b[k][q] != -1:
                            ans = b[i][l] + b[j][g] + b[k][q]
print(ans)
