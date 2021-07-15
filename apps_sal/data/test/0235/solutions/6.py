n = int(input())
l = 1
r = n
while l < r:
    m = (l + r) // 2
    cur = n
    k = m
    p = 0
    v = 0
    while cur:
        v += min(cur, k)
        cur -= min(cur, k)
        p += cur // 10
        cur -= cur // 10
    if v >= (n + 1) // 2:
        r = m
    else:
        l = m + 1
print(l)

