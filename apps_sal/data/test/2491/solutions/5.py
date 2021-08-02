n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    edges.append((a, b, -c))

dist = [float('inf')] * n
dist[0] = 0
for i in range(n - 1):
    # n-1回ループすることで、到達できるすべての頂点の更新ができる
    for st, en, score in edges:
        if dist[st] == float('inf'): continue
        if dist[en] > dist[st] + score:
            dist[en] = dist[st] + score

negative = [False] * n

for loop in range(n):
    # n回目以降のループで更新された頂点は負閉路を含む
    # それをn回繰り返して更新された頂点は、負閉路の影響を受けている
    for e in edges:
        st, en, score = e
        if dist[st] == float('inf'): continue
        if dist[en] > dist[st] + score:
            dist[en] = dist[st] + score
            negative[en] = True
        if negative[st]:
            negative[en] = True

if negative[n - 1]:
    print('inf')
else:
    print(-dist[n - 1])
