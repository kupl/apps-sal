s = input().split('T')
(gx, gy) = map(int, input().split())
for (i, e) in enumerate(s):
    s[i] = len(e)
(xs, ys) = (s[::2], s[1::2])
x = xs.pop(0) if len(xs) > 0 else 0
y = 0
xs.sort(reverse=True)
ys.sort(reverse=True)


def c(p, g, lis):
    for e in lis:
        if p <= g:
            p += e
        else:
            p -= e
    return p == g


if c(x, gx, xs) and c(y, gy, ys):
    print('Yes')
else:
    print('No')
