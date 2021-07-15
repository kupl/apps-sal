def inpmap():
    return list(map(int, input().split()))
n, a, b, c, t = inpmap()
arr = inpmap()
if b >= c:
    print(a * n)
else:
    s = 0
    for x in arr:
        # print(s)
        s += a - (t - x) * b
        # print(a - (t - x) * b, (t - x) * c)
        s += (t - x) * c
    print(s)

