(n, m) = map(int, input().split())
edge = []
for _ in range(m):
    (a, b, c) = map(int, input().split())
    edge.append([a - 1, b - 1, -c])
d = [float('inf') for _ in range(n)]
d[0] = 0
check = [0 for _ in range(n)]
for i in range(n):
    for (now, next, weight) in edge:
        if d[next] > d[now] + weight:
            d[next] = d[now] + weight
            if i == n - 1:
                check[next] = 1
        if i == n - 1:
            if check[now]:
                check[next] = 1
if check[-1]:
    print('inf')
else:
    print(-d[-1])
