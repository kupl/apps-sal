def rd():
    return list(map(int, input().split()))


(n, p, m) = rd()
(q, l, r) = (0, 0, 0)
for i in range(n):
    (d, t) = rd()
    c = d - q - 1
    r += max(min(c - l // p, c), 0)
    l -= p * (c + 1) - t
    r += l < 0
    q = d
c = m - q
print(r + max(min(c - l // p, c), 0))
