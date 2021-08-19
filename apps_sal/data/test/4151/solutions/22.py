MOD = 998244353


def pwr(x, y):
    if y == 0:
        return 1
    p = pwr(x, y // 2) % MOD
    p = p * p % MOD
    if y % 2 == 0:
        return p
    else:
        return x * p % MOD


n = int(input())
a = list(map(int, input().split()))
c = 0
f = [0] * n
d = {}
for i in range(n):
    d[a[i]] = i
for i in range(n):
    if i == 0:
        c = 0
    elif f[i] == 0:
        c += 1
    if f[i] == 0:
        j = i + 1
        k = d[a[i]]
        while j <= k:
            f[j] = 1
            k = max(k, d[a[j]])
            j += 1
ans = pwr(2, c)
print(ans)
