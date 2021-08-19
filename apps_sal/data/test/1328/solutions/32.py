INF = float('inf')
MAXAB = 10
(n, ma, mb) = list(map(int, input().split()))
t = [[INF] * (n * MAXAB + 1) for _ in range(n * MAXAB + 1)]
t[0][0] = 0
for _ in range(n):
    (a, b, c) = list(map(int, input().split()))
    for aa in range(n * MAXAB, -1, -1):
        for bb in range(n * MAXAB, -1, -1):
            if t[aa][bb] == INF:
                continue
            if t[a + aa][b + bb] > t[aa][bb] + c:
                t[a + aa][b + bb] = t[aa][bb] + c
result = INF
for a in range(1, n * MAXAB + 1):
    for b in range(1, n * MAXAB + 1):
        if a * mb == b * ma and result > t[a][b]:
            result = t[a][b]
if result == INF:
    result = -1
print(result)
