n, m = list(map(int, input().split(' ')))

if n % 2 == 0:
    l = -1 + n // 2
    h = n // 2
    k = l * (l + 1) // 2 + h * (h + 1) // 2
else:
    z = n // 2
    k = z * (z + 1)
ans = 0
for i in range(m):
    x, d = list(map(int, input().split(' ')))
    ans += n * x

    if d >= 0:
        ans += d * ((n * (n - 1)) // 2)
    else:
        ans += d * k

print(ans / n)
