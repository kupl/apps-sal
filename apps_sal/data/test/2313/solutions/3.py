n = int(input())
c = list(map(int, input().split()))
mod = 998244353
inv = pow(n, mod - 2, mod)
c.sort()
imos = [c[i] for i in range(n)]
for i in range(1, n):
    imos[i] += imos[i - 1]
res = [0] * n
for i in range(1, n + 1):
    temp = 0
    L = n - i
    R = n - 1
    count = 0
    while True:
        temp += count * (imos[R] - imos[L - 1] * (L >= 1))
        count += 1
        if L == 0:
            break
        else:
            R -= i
            L = max(0, L - i)
    res[i - 1] = temp * inv % mod
print(*res)
