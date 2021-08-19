n = int(input())


def j(i):
    return 3 * i * (i + 1) <= n


high = 10 ** 18
low = 0
while high - low > 5:
    mid = high + low >> 1
    if j(mid):
        low = mid
    else:
        high = mid
while j(low + 1):
    low += 1
r = low
x = r << 1
y = 0
n -= 3 * r * (r + 1)
r += 1
if n:
    n -= 1
    x += 1
    y += 2
if n:
    sub = min(n, r - 1)
    n -= sub
    x -= sub
    y += sub << 1
if n:
    sub = min(n, r)
    n -= sub
    x -= sub << 1
if n:
    sub = min(n, r)
    n -= sub
    x -= sub
    y -= sub << 1
if n:
    sub = min(n, r)
    n -= sub
    x += sub
    y -= sub << 1
if n:
    sub = min(n, r)
    n -= sub
    x += sub << 1
if n:
    sub = min(n, r)
    n -= sub
    x += sub
    y += sub << 1
print(x, y)
