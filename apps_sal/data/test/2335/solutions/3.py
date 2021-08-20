k = int(input())
(t, a, b, m, n, o, d, e, s, x, y, z, l) = 13 * [0]
for i in range(k):
    c = input().split(' ')
    f = int(c[0])
    if c[1] == 'G':
        if o < 1:
            z = f
        if t:
            if m > 0:
                d = max(d, f - m)
            if n > 0:
                e = max(e, f - n)
            s += min(2 * (f - o), 3 * (f - o) - d - e)
        (d, e, a, b) = 4 * [0]
        m = f
        n = f
        o = f
        t = 1
        l += 1
    if c[1] == 'R':
        a += 1
        if m < 1:
            x = f
        if m > 0 and t:
            d = max(d, f - m)
        m = f
    if c[1] == 'B':
        b += 1
        if n < 1:
            y = f
        if n > 0 and t:
            e = max(e, f - n)
        n = f
if l > 0:
    if a > 0:
        s += m - o
    if b > 0:
        s += n - o
    if x > 0:
        s += z - x
    if y > 0:
        s += z - y
else:
    s = m - x + n - y
print(s)
