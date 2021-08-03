import math
n, r = map(int, input().split())
xs = list(map(int, input().split()))


def ch(c1, c2):
    d = abs(c1[0] - c2[0])
    ph = math.sqrt(2 * 2 * r * r - d * d)
    return c2[1] + ph


cs = []
for i in range(len(xs)):
    h = r
    x = xs[i]
    for c in cs:
        if abs(x - c[0]) > 2 * r:
            continue
        else:
            h = max(h, ch([x, h], c))
    cs.append([x, h])

print(' '.join([str(i[1]) for i in cs]))
