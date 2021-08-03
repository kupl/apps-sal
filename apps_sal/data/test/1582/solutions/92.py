N = int(input())

X = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1, N + 1):
    s = str(i)
    a, b = int(s[0]), int(s[-1])
    X[a][b] += 1

ans = 0
for a in range(10):
    for b in range(10):
        ans += X[a][b] * X[b][a]

print(ans)
