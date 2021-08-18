def inpmap():
    return list(map(int, input().split()))


n, a, b, c, t = inpmap()
arr = inpmap()
if b >= c:
    print(a * n)
else:
    s = 0
    for x in arr:
        s += a - (t - x) * b
        s += (t - x) * c
    print(s)
