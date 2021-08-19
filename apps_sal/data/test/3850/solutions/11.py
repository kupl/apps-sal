def read():
    return list(map(int, input().split()))


(n, k, p) = read()
a = list(read())
b = list(read())
a.sort()
b.sort()


def cal(a, b):
    return abs(a - b) + abs(b - p)


mi = 1000000000000000.0
for _ in range(k - n + 1):
    ma = 0
    for __ in range(n):
        te = cal(a[__], b[_ + __])
        if te > ma:
            ma = te
    if ma < mi:
        mi = ma
print(mi)
