(n, le) = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a)
l = -1
r = 10 ** 9 + 10 ** 5
for i in range(1000):
    m = (r + l) / 2
    fail = False
    for i in range(len(a) - 1):
        if not a[i] + 2 * m >= a[i + 1]:
            fail = True
            break
    if not fail:
        r = m
    else:
        l = m
print(max(min(a), le - max(a), (l + r) / 2))
