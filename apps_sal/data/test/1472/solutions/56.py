(n, x, y) = list(map(int, input().split()))
(x, y) = (x - 1, y - 1)
ans = [0] * (n - 1)
for i in range(n - 1):
    for j in range(i + 1, n):
        d = min(j - i, abs(x - i) + 1 + abs(j - y), abs(y - i) + 1 + abs(j - x))
        ans[d - 1] += 1
for a in ans:
    print(a)
