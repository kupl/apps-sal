(h, w, a, b) = list(map(int, input().split()))
fac = [0] * 200001
inv = [0] * 200001
fac[0] = 1
ans = 0
for i in range(1, 200001):
    fac[i] = fac[i - 1] * i % 1000000007
inv[200000] = pow(fac[200000], 1000000005, 1000000007)
for i in range(199999, 0, -1):
    inv[i] = inv[i + 1] * (i + 1) % 1000000007
    inv[0] = 1
for i in range(h - a):
    if i == 0:
        if h == 1:
            x = 1
        else:
            x = fac[w - b + h - 2 - i] * inv[w - 1 - b] * inv[h - 1 - i] % 1000000007
    else:
        x = fac[b - 1 + i] * inv[b - 1] * inv[i] % 1000000007 * (fac[w - b + h - 2 - i] * inv[w - b - 1] * inv[h - 1 - i] % 1000000007)
    ans = (ans + x) % 1000000007
print(ans)
