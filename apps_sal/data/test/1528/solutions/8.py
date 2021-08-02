n, x = map(int, input().split())
l, p = [1], [1]
for i in range(n):
    l += [l[-1] * 2 + 3]
    p += [p[-1] * 2 + 1]
x -= 1
a = 0
while x > 0 and n:
    t = l[n] // 2
    if x >= t:
        a += p[n - 1] + 1
        x -= t
    x -= 1
    n -= 1
if x >= 0 and n == 0: a += 1
print(a)
