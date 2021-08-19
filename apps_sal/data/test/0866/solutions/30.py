def com(n, r, m):
    f = [1, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] * i % m)
    return f[n] * pow(f[r] * f[n - r] % m, m - 2, m) % m


mod = 10 ** 9 + 7
(x, y) = map(int, input().split())
z = (x + y) // 3
if (x + y) % 3 or abs(x - y) > z:
    ans = 0
else:
    ans = com(z, x - z, mod)
print(ans)
