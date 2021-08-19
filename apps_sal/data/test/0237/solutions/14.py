def check(n, m, k, r):
    a = r - k
    u = 0
    if a > 0:
        u += (a + r) * (k + 1) // 2
    else:
        u += r * (r + 1) // 2
    b = r - (n - 1 - k)
    v = 0
    if b > 0:
        v += (b + r) * (n - k) // 2
    else:
        v += r * (r + 1) // 2
    t = u + v - r
    return t <= m


(n, m, k) = list(map(int, input().split()))
k -= 1
m -= n
INF = 10 ** 9 + 10
a = 0
b = INF
while b - a > 1:
    mid = (a + b) // 2
    if check(n, m, k, mid):
        a = mid
    else:
        b = mid
res = 1 + a
print(res)
