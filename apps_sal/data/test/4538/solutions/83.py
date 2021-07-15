from math import sqrt as r
N, D = map(int, input().split())

ans = 0

for i in range(N):
    X, Y = map(int, input().split())
    d = r(X**2 + Y**2)
    if d <= D:
        ans += 1

print(ans)
