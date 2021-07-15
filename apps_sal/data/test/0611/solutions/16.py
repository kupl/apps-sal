n, m = map(int, input().split())
ans = 0
s1 = (n * (n - 1)) // 2
fi = n // 2
se = n - fi - 1
s2 = (fi * (fi + 1)) // 2 + (se * (se + 1)) // 2
for i in range(m):
    x, d = map(int, input().split())
    if d < 0:
        ans += n * x + d * s2
    else:
        ans += n * x + d * s1
print(ans / n)
