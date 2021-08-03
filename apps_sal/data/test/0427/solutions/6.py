c1, c2, x, y = map(int, input().split())
xy = x * y
n = 1
while n - n // x < c1 or n - n // y < c2 or n - n // xy < c1 + c2:
    n = n << 1

l = 1
r = n
while r - l > 1:
    m = (r + l) >> 1
    if m - m // x < c1 or m - m // y < c2 or m - m // xy < c1 + c2:
        l = m
    else:
        r = m
m = l
if m - m // x < c1 or m - m // y < c2 or m - m // xy < c1 + c2:
    print(r)
else:
    print(l)
