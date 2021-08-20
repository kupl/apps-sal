def mp():
    return map(int, input().split())


(n, k) = mp()
a = list(mp())
a.sort()
l = 1
r = 10 ** 20
while l + 1 < r:
    m = (l + r) // 2
    s = 0
    for i in range(n // 2, n):
        s += max(0, m - a[i])
    if k < s:
        r = m
    else:
        l = m
print(l)
