w, m, k = list(map(int, input().split()))
d, v = len(str(m)), 0
c = min(10 ** d - m, w // (k * d))
while c:
    v += c
    w -= c * k * d
    m = 10 ** d
    d += 1
    c = min(10 ** d - m, w // (k * d))
print(v)

