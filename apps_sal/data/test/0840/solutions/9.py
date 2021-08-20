def ok(u, a, b, n, k):
    for i in range(n):
        if b[i] >= a[i] * u:
            continue
        else:
            k -= a[i] * u - b[i]
            if k < 0:
                return False
    return k >= 0


(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
(l, r) = (0, 2000000010)
while l < r - 1:
    g = (l + r) // 2
    if ok(g, a, b, n, k):
        l = g
    else:
        r = g
print(l)
