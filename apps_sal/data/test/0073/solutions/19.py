(c, v0, v1, a, l) = map(int, input().split(' '))
days = 0
while c > 0:
    if days > 0:
        c += l
    c -= v0
    v0 += a
    if v1 < v0:
        v0 = v1
    days += 1
print(days)
