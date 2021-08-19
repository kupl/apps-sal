(c, v0, v1, a, l) = [int(i) for i in input().split()]
(i, d) = (1, 0)
while 1:
    if d > 0:
        i -= l
    v = min(v0 + d * a, v1)
    d += 1
    i += v
    if i > c:
        break
print(d)
