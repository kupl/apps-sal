n, *t = map(int, open(0).read().split())
*z, = zip(t[::2], t[1::2])
s = set((a + b) % 2for a, b in z)
if len(s) > 1:
    print(-1)
    return
s, *_ = s
d = [2**(38 - i)for i in range(39)] + [1] * (s < 1)
print(len(d), *d)
for a, b in z:
    x = y = 0
    o = ''
    for i in d:
        if abs(a - x) > abs(b - y):
            f = a - x > 0
            o += 'LR'[f]
            x += i * f or -i
        else:
            f = b - y > 0
            o += 'DU'[f]
            y += i * f or -i
    print(o)
