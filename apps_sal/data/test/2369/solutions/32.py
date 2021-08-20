(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
p = [1]
mod = 10 ** 9 + 7
for i in range(n):
    p.append(p[-1] * (i + 1) % mod)
p.pop()


def comb(n, k, mod):
    s = p[n] * pow(p[k], mod - 2, mod) % mod
    s = s * pow(p[n - k], mod - 2, mod) % mod
    return s


max_sum = 0
min_sum = 0
for i in range(n - k + 1):
    max_sum += a[-(i + 1)] * comb(n - 1 - i, k - 1, mod)
    max_sum = max_sum % mod
    min_sum += a[i] * comb(n - 1 - i, k - 1, mod)
    min_sum = min_sum % mod
ans = max_sum - min_sum
if ans < 0:
    ans += mod
print(ans)
