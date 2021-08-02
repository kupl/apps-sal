n, m = map(int, input().split())
l = 0
r = 10 ** 18 + 1
d = n - m
while r - l > 1:
    mi = (r + l) // 2
    if d > mi * (mi + 1) // 2:
        l = mi
    else:
        r = mi
if n > m:
    print(r + m)
else:
    print(n)
