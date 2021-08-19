def cnt(x, y):
    return y - x


(w, m, k) = list(map(int, input().split()))
(p, d, res) = (1, 0, 0)
while p <= m:
    p *= 10
    d += 1
while cnt(m, p) * d * k <= w:
    w -= cnt(m, p) * d * k
    res += cnt(m, p)
    m = p
    p *= 10
    d += 1
res += w // (d * k)
print(res)
