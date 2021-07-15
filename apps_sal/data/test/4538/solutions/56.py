N, D = map(int, input().split())
ans = 0

for  i in range(N):
    x, y = map(int, input().split())
    d = (x**2 + y**2) ** 0.5
    if d <= D:
        ans += 1

print(ans)
