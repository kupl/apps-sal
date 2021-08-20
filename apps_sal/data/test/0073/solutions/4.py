3


def read_ints():
    return [int(i) for i in input().split()]


(c, v0, v1, a, l) = read_ints()
s = 0
d = 1
while s < c:
    s = min(s + v0, c)
    if s == c:
        break
    v0 = min(v0 + a, v1)
    s -= l
    d += 1
print(d)
