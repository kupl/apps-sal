(n, m) = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
a.sort()
b.sort()
c = list(set(a + b))
c.sort()
ans = 1e+18
less = 0
big = sum(b)
(i1, k1) = (0, 0)
(i2, k2) = (0, len(b))
for border in c:
    while i1 < len(a) and a[i1] < border:
        less += a[i1]
        i1 += 1
        k1 += 1
    while i2 < len(b) and b[i2] < border:
        big -= b[i2]
        i2 += 1
        k2 -= 1
    ans = min(ans, border * k1 - less + big - border * k2)
print(int(ans))
