(n, m) = map(int, input().split())
ans = 0
for i in range(m):
    (x, d) = map(int, input().split())
    ans += x * n
    if d >= 0:
        r = n * (n - 1) // 2
        ans += r * d
    elif n % 2 != 0:
        r = n // 2
        r = r * (r + 1)
        ans += r * d
    else:
        r = n // 2
        k = r - 1
        r = r * (r + 1) // 2 + k * (k + 1) // 2
        ans += r * d
print(ans / n)
