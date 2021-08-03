N = int(input())
x = [0 for _ in range(N)]
y = [0 for _ in range(N)]

for i in range(N):
    x[i], y[i] = map(int, input().split())

X = [0 for _ in range(N)]
Y = [0 for _ in range(N)]

for i in range(N):
    X[i], Y[i] = x[i] - y[i], x[i] + y[i]

ans = 0
ans = max(max(X) - min(X), max(Y) - min(Y))

print(ans)
