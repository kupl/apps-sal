def f(a, b):
    return min(2 * a - b + 1, b - 1)


n, k = map(int, input().split())
ans = 0
for i in range(2, 2 * n + 1):
    if not (2 <= i - k <= 2 * n):
        continue
    ans += f(n, i) * f(n, i - k)
print(ans)
