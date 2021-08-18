n, m = map(int, input().split())
abc = [tuple(map(int, input().split())) for _ in range(m)]
Inf = float('inf')
dist = [Inf] * n
dist[0] = 0
for i in range(n):
    for a, b, c in abc:
        a, b, c = a - 1, b - 1, -c
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            if i == n - 1 and b == n - 1:
                print('inf')
                return
print(-dist[-1])
