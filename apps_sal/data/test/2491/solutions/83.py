n, m = list(map(int, input().split()))
a = [0] * m
b = [0] * m
c = [0] * m
INF = float('inf')
dist = [INF] * n
dist[0] = 0
for i in range(m):
    a[i], b[i], c[i] = list(map(int, input().split()))
    a[i] -= 1
    b[i] -= 1
    c[i] *= -1
for loop in range(n - 1):
    for i in range(m):
        if dist[a[i]] == INF:
            continue
        if dist[b[i]] > dist[a[i]] + c[i]:
            dist[b[i]] = dist[a[i]] + c[i]
ans = dist[n - 1]

neg = [False] * n
for loop in range(n):
    for i in range(m):
        if dist[b[i]] > dist[a[i]] + c[i]:
            dist[b[i]] = dist[a[i]] + c[i]
            neg[b[i]] = True
        if neg[a[i]]:
            neg[b[i]] = True
if neg[n - 1]:
    print('inf')
else:
    print((-ans))
