INF = float('inf')
(n, ma, mb) = list(map(int, input().split()))
t = [[INF] * 401 for _ in range(401)]
t[0][0] = 0
for _ in range(n):
    (a, b, c) = list(map(int, input().split()))
    for aa in range(400, -1, -1):
        for bb in range(400, -1, -1):
            if t[aa][bb] == INF:
                continue
            if t[a + aa][b + bb] > t[aa][bb] + c:
                t[a + aa][b + bb] = t[aa][bb] + c
result = INF
for a in range(400, 0, -1):
    for b in range(400, 0, -1):
        if a * mb == b * ma and t[a][b] < result:
            result = t[a][b]
if result == INF:
    result = -1
print(result)
