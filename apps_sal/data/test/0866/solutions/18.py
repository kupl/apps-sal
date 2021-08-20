def CombiMod(n, r, mod):
    if n < r:
        return 0
    if n - r < r:
        r = n - r
    comb = 1
    for x in range(n - r + 1, n + 1):
        comb = comb * x % mod
    d = 1
    for x in range(1, r + 1):
        d = d * x % mod
    comb *= pow(d, mod - 2, mod)
    return comb % mod


(x, y) = map(int, input().split())
if (x + y) % 3:
    ans = 0
else:
    n = (x + y) // 3
    x -= n
    y -= n
    if x < 0 or y < 0:
        ans = 0
    else:
        ans = CombiMod(x + y, y, 10 ** 9 + 7)
print(ans)
