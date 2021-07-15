n = int(input())
d = {}
for i in range(n - 1):
    u, v = map(int, input().split())
    if u not in d:
        d[u] = 1
    else:
        d[u] += 1
    if v not in d:
        d[v] = 1
    else:
        d[v] += 1
ans = 0
for i in range(1, n + 1):
    if d[i] == 1:
        ans += 1
print(ans)
