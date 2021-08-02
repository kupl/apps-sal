n, x, y = list(map(int, input().split()))

ans = 0
ans = [0] * (n - 1)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        now = min(j - i, abs(j - y) + abs(i - x) + 1)
        ans[now - 1] += 1

for i in ans:
    print(i)
