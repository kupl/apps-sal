n, x, y = map(int, input().split())
ans = [0] * n
for i in range(1, n):
    for j in range(i + 1, n + 1):
        a = min(j - i, abs(x - i) + 1 + abs(j - y), abs(y - i) + 1 + abs(j - x))
        ans[a] += 1
for i in range(1, n):
    print(ans[i])
