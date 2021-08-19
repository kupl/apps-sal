(a, b, x) = list(map(int, input().split()))
r = 10 ** 9 + 1
l = 0
while r - l > 1:
    m = (r + l) // 2
    p = a * m + b * len(str(m))
    if p > x:
        r = m
    else:
        l = m
print(l)
