def f(x): return x // 3


r, g, b = list(map(int, input().split()))
m = min(r, g, b)
ans = 0
for i in range(max(0, m - 30), m + 1):
    ans = max(ans, i + f(r - i) + f(g - i) + f(b - i))
print(ans)
