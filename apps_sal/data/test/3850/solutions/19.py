def good(n, k, p, a, b, x):
    j = 0
    c = 0
    for i in range(n):
        while j < k:
            if abs(a[i] - b[j]) + abs(b[j] - p) <= x:
                j += 1
                c += 1
                break
            j += 1
    return c == n


(n, k, p) = [int(x) for x in input().split(' ')]
a = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]
a.sort()
b.sort()
l = -1
r = 2 * 10 ** 9
while r - l > 1:
    m = (l + r) // 2
    if good(n, k, p, a, b, m):
        r = m
    else:
        l = m
print(r)
