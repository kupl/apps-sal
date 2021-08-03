n, x, y = list(map(int, input().split()))

ans = [0 for _ in range(n - 1)]

for i in range(n - 1):
    for j in range(i + 1, n):
        t = i + 1
        u = j + 1
        H = min(abs(u - t), abs(t - x) + 1 + abs(y - u), abs(t - y) + 1 + abs(x - u))
        ans[H - 1] += 1

for l in ans:
    print(l)
