F = [1, 1]
for i in range(2, 1001):
    F.append(F[-1] * i)


def ncr(x, y):
    return F[x] // (F[y] * F[x - y])


n, m = list(map(int, input().split()))
P = [0] * 2000

for j in range(1, min(m, n) + 1):
    mine = m
    total = n * m
    p = 1
    for x in range(j):
        p *= mine / total
        mine -= 1
        total -= 1
    for x in range(n - j):
        p *= (total - mine) / total
        total -= 1
    p *= n
    p *= ncr(n, j)
    P[j] = p

ans = 0

for j in range(1, min(m, n) + 1):
    p = P[j]
    ans += P[j] * (j * j) / (n * n)
print(ans)
