from math import factorial as f


def C(n, m):
    if n < m: return 0
    return f(n) // (f(n - m) * f(m))


m, k = map(int, input().split())
ans = 1
for bit in reversed(range(65)):
    if k == 0:
        break
    if C(bit, k - 1) < m:
        ans += (1 << bit)
        m -= C(bit, k - 1)
        k -= 1
print(ans)
