N, M = map(int, input().split())
req = []
for i in range(M):
    a, b = map(int, input().split())
    req.append([a, b])

req = sorted(req, key=lambda x: x[1])

ans = 1
current = req[0][1]
for i in range(1, len(req)):
    if req[i][0] < current:
        continue
    current = req[i][1]
    ans += 1
print(ans)
