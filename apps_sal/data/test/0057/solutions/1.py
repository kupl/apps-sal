n = int(input())

X = []
Y = []
for i in range(n):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)

dx = max(X) - min(X)
dy = max(Y) - min(Y)

ans = dx * dy
if (ans > 0):
    print(ans)
else:
    print(-1)


