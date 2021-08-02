c, v0, v1, a, l = map(int, input().split())
n = 0
while c > 0:
    c -= v0
    v0 = min(v0 + a, v1)
    if n > 0:
        c += l
    n += 1
print(n)
