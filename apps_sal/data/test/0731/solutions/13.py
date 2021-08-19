(w, m, k) = tuple(map(int, input().split()))
s = len(str(m))
t = m
n = 10 ** s
r = (n - t) * s * k
while w >= r:
    w -= r
    t = n
    n *= 10
    s += 1
    r = (n - t) * s * k
if w != 0:
    n //= 10
    if n < m:
        n = 0
    else:
        n -= m
    r = s * k
    n += w // r
else:
    n = n // 10 - m
print(n)
