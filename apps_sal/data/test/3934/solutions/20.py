n = int(input())
adj = [[] for i in range(n)]
for _ in range(n - 1):
    (u, v) = map(int, input().split())
    adj[u - 1].append(v)
    adj[v - 1].append(u)
for v in adj:
    if len(v) == 2:
        print('NO')
        break
else:
    print('YES')
